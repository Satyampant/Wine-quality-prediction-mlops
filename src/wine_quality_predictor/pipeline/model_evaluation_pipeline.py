from src.wine_quality_predictor.config.configuration import ConfigurationManager
from src.wine_quality_predictor.components.model_evaluation import ModelEvaluation
from src.wine_quality_predictor import logger

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()