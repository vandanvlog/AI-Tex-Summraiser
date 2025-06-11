from ai_text_summariser.pipline.stage_01_dataingestion import DataIngestionTrainingPipline
from ai_text_summariser.logging import logger
from ai_text_summariser.pipline.stage_02_datavalidation import DataValidationTrainingPipline
from ai_text_summariser.pipline.stage_03_datatransformation import DataTransformationTrainingPipline
from ai_text_summariser.pipline.stage_04_model_trainner import ModelTrainnerTrainingPipline
from ai_text_summariser.pipline.stage_05_model_evaluation import ModelEvaluationTrainingPipline

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



STAGE_NAME = "Model Trainner Stage"
try:
    logger.info(f">>> stage {STAGE_NAME} is strted <<<")
    model_trainner = ModelTrainnerTrainingPipline()
    model_trainner.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e