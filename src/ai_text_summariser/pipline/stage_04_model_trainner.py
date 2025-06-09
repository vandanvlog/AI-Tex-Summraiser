from ai_text_summariser.config.configuration import ConfigurationManager
from ai_text_summariser.components.model_trainner import ModelTrainer
from ai_text_summariser.logging import logger

class ModelTrainnerTrainingPipline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()