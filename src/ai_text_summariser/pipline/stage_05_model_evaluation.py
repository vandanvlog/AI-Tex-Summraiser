from ai_text_summariser.config.configuration import ConfigurationManager
from ai_text_summariser.components.modelevaluation import ModelEvaluation
from ai_text_summariser.logging import logger

class ModelEvaluationTrainingPipline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()