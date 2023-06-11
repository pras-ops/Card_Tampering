import os
import sys
from skimage.metrics import structural_similarity
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
import imutils
import cv2
from PIL import Image
import numpy as np
from src.components.data_ingestion import DataIngestion



@dataclass
class DataTransformationConfig:
    transformed_data_path: str = os.path.join('artifacts', 'transformed.png')
    

class DataTransformation:
    def __init__(self):
        self.transformation_config = DataTransformationConfig()
        self.data_ingestion = DataIngestion()  # Create an instance of DataIngestion

    def perform_image_transformation(self):
        try:
           
            # Load the original image
            original_image = Image.open(self.data_ingestion.ingestion_config.original_image_path)
            logging.info("Importing Saved original image")
            # Load the uploaded image
            uploaded_image = Image.open(self.data_ingestion.ingestion_config.tampered_image_path)
            logging.info("Importing Saved Tampered image")

            # Convert PIL images to numpy arrays
            original_np = np.array(original_image)
            uploaded_np = np.array(uploaded_image)
            logging.info("Convert PIL images to numpy arrays")

            # Resize both images to the desired size
            size = (250, 160)
            original_np = cv2.resize(original_np, size)
            uploaded_np = cv2.resize(uploaded_np, size)
            logging.info("Resize both images")

            # Convert images to grayscale
            original_gray = cv2.cvtColor(original_np, cv2.COLOR_RGB2GRAY)
            uploaded_gray = cv2.cvtColor(uploaded_np, cv2.COLOR_RGB2GRAY)
            logging.info("Convert images to grayscale")

            # Convert PIL Images to NumPy arrays
            original_gray_array = np.array(original_gray)
            uploaded_gray_array = np.array(uploaded_gray)
            logging.info("Convert PIL Images to NumPy arrays")

            # Calculate structural similarity
            (score, diff) = structural_similarity(original_gray_array, uploaded_gray_array, full=True)
            diff = (diff * 255).astype("uint8")
            logging.info("Calculate structural similarity")

            # Calculate threshold and contours
            thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            logging.info("Calculate threshold and contours")

            # Convert PIL Images to NumPy arrays
            original_image_drawn = np.array(original_image)
            uploaded_image_drawn = np.array(uploaded_image)
            logging.info("Convert PIL Images to NumPy arrays")

            for c in cnts:
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(original_image_drawn, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.rectangle(uploaded_image_drawn, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Save the transformed images
            os.makedirs(self.transformation_config.transformed_data_path, exist_ok=True)

            #transformed_images_dir = 'Card_Tampering/artificatas/transformed'
            #os.makedirs(transformed_images_dir, exist_ok=True)

            original_image_drawn = Image.fromarray(original_image_drawn)
            original_image_drawn.save(os.path.join(self.transformation_config.transformed_data_path, 'original_transformed.jpg'))
            logging.info("Save the transformed images original_image_drawn")

            uploaded_image_drawn = Image.fromarray(uploaded_image_drawn)
            uploaded_image_drawn.save(os.path.join(self.transformation_config.transformed_data_path, 'uploaded_transformed.jpg'))
            logging.info("Save the transformed images uploaded_image_drawn")


            return round(score * 100, 2)
        
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == '__main__':
    obj = DataTransformation()
    score = obj.perform_image_transformation()

    print(f"Structural similarity score: {score}%")