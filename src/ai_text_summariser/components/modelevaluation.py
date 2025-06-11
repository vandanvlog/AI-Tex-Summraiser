from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import evaluate
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import pandas as pd
from tqdm import tqdm
from ai_text_summariser.entity import ModelEvaluationconfig
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationconfig):
        self.config = config

    def generate_batch_sized_chunks(self, elements, batch_size):
        for i in range(0, len(elements), batch_size):
            yield elements[i: i + batch_size]

    def calculate_metric_on_test_ds(self, dataset, metric, model, tokenizer,
                                    batch_size=16, device="cuda" if torch.cuda.is_available() else "cpu",
                                    column_text="article", column_summary="highlights"):
        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size))
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size))

        for article_batch, target_batch in tqdm(zip(article_batches, target_batches), total=len(article_batches)):
            inputs = tokenizer(article_batch, max_length=1024, truncation=True,
                               padding="max_length", return_tensors="pt")

            summaries = model.generate(
                input_ids=inputs["input_ids"].to(device),
                attention_mask=inputs["attention_mask"].to(device),
                length_penalty=0.8, num_beams=8, max_length=128
            )

            decoded_summaries = [
                tokenizer.decode(s, skip_special_tokens=True, clean_up_tokenization_spaces=True)
                for s in summaries
            ]

            metric.add_batch(predictions=decoded_summaries, references=target_batch)

        return metric.compute()

    def evaluate(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"

        tokenizer_path = Path(self.config.tokenizer_path).resolve()
        model_path = Path(self.config.model_path).resolve()

        if not tokenizer_path.exists():
            raise FileNotFoundError(f"Tokenizer path does not exist: {tokenizer_path}")
        if not model_path.exists():
            raise FileNotFoundError(f"Model path does not exist: {model_path}")

        tokenizer = AutoTokenizer.from_pretrained(tokenizer_path.as_posix(), local_files_only=True)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(model_path.as_posix(), local_files_only=True).to(device)

        dataset_samsum_pt = load_from_disk(self.config.data_path)

        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
        rouge_metric = evaluate.load("rouge")

        score = self.calculate_metric_on_test_ds(
            dataset_samsum_pt["test"][:10], rouge_metric, model_pegasus, tokenizer,
            batch_size=2, column_text="dialogue", column_summary="summary"
        )

        rouge_dict = {rn: round(score[rn], 4) for rn in rouge_names}
        df = pd.DataFrame(rouge_dict, index=["pegasus"])
        df.to_csv(self.config.metric_file_name, index=False)


