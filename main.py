from ai_text_summariser.pipline.stage_01_dataingestion import DataIngestionTrainingPipline
from ai_text_summariser.logging import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>> stage {STAGE_NAME} is strted <<<")
    data_ingestion = DataIngestionTrainingPipline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e