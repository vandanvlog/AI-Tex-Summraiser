from ai_text_summariser.pipline.stage_01_dataingestion import DataIngestionTrainingPipline
from ai_text_summariser.logging import logger
from ai_text_summariser.pipline.stage_02_datavalidation import DataValidationTrainingPipline
from ai_text_summariser.pipline.stage_03_datatransformation import DataTransformationTrainingPipline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>> stage {STAGE_NAME} is strted <<<")
    data_ingestion = DataIngestionTrainingPipline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>> stage {STAGE_NAME} is strted <<<")
    data_validation = DataValidationTrainingPipline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>> stage {STAGE_NAME} is strted <<<")
    data_transformation = DataTransformationTrainingPipline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e



