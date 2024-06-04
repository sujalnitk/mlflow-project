from mlproject.config.configuration import ConfigurationManger
from mlproject.components.model_trainer import ModelTrainer
from mlproject import logger


STAGE_NAME = "Model Trainer Stage"



class ModelTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e