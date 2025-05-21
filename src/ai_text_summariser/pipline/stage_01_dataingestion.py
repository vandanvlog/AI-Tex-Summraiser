from ai_text_summariser.config.configuration import ConfigurationManager
from ai_text_summariser.components.dataingestion import DataIngestion
from ai_text_summariser.logging import logger


class DataIngestionTrainingPipline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
