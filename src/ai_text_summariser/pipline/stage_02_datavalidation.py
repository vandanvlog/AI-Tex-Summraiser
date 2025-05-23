from ai_text_summariser.config.configuration import ConfigurationManager
from ai_text_summariser.components.datavalidation import DataValiadtion
from ai_text_summariser.logging import logger


class DataValidationTrainingPipline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()
