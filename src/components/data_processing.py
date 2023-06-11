from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation


def data_processing():
    # Create instances of DataIngestion and DataTransformation
    ingestion = DataIngestion()
    transformation = DataTransformation()

    # Perform data ingestion
    ingestion_result = ingestion.download_images()

    # Perform data transformation
    transformation_result = transformation.perform_image_transformation()

    # Return the results
    return ingestion_result, transformation_result


if __name__ == '__main__':
    try:
        ingestion_result, transformation_result = data_processing()

        print("Data Ingestion Result:", ingestion_result)
        print("Data Transformation Result:", transformation_result)

    except Exception as e:
        print("Error occurred during data processing:", str(e))
