import requests
import os
import sys
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from PIL import Image

@dataclass
class DataIngestionConfig:
    original_image_path: str=os.path.join('artifacts',"original_image.png")
    tampered_image_path: str=os.path.join('artifacts',"tampered_image.png")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()   

    def download_images(self):
        logging.info("Initiated Downloading Images")
        try:
            # Download the original image
            original_image_url = 'https://www.thestatesman.com/wp-content/uploads/2019/07/pan-card.jpg'
            original_image = Image.open(requests.get(original_image_url, stream=True).raw)
            
            os.makedirs(os.path.dirname(self.ingestion_config.original_image_path),exist_ok=True)
            original_image_rgb = original_image.convert("RGB")  # Convert to RGB mode
            original_image_rgb.save(self.ingestion_config.original_image_path)


            logging.info("Importing Original Image")
            # Download the tampered image
            tampered_image_url = 'https://assets1.cleartax-cdn.com/s/img/20170526124335/Pan4.png'
            tampered_image = Image.open(requests.get(tampered_image_url, stream=True).raw)
            tampered_image_rgb = tampered_image.convert("RGB")  # Convert to RGB mode
            tampered_image_rgb.save(self.ingestion_config.tampered_image_path)

            logging.info("Importing tampered Image")
        
            return(
                self.ingestion_config.original_image_path,
                self.ingestion_config.tampered_image_path

            ) 
    
        except Exception as e:
            raise CustomException(e,sys)


#def main(self):
    # Download images
#    original_image, tampered_image = download_images()

    # Perform any further processing or data ingestion tasks here

    # Display the images (optional)
#    original_image.show()
#    tampered_image.show()

if __name__ == '__main__':
    obj=DataIngestion()
    original_image, tampered_image=obj.download_images()

