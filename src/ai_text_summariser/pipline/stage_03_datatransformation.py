from ai_text_summariser.config.configuration import ConfigurationManager
from ai_text_summariser.components.datatransformation import DataTransformation
from ai_text_summariser.logging import logger

class DataTransformationTrainingPipline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()