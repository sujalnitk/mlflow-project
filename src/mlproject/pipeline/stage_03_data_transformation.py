from mlproject.config.configuration import ConfigurationManger
from mlproject.components.data_transformation import DataTransformation
from mlproject import logger
from pathlib import Path


STAGE_NAME = 'Data Transformation Stage'

class DataTransfomationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManger()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()

            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            print(e)

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransfomationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e