import requests
import os
import sys
from src.exception import CustomException
from src.logger import logging
from PIL import Image


def download_images():
    logging.info("Initiated Downloading Images")
    try:
        # Download the original image
        original_image_url = 'https://www.thestatesman.com/wp-content/uploads/2019/07/pan-card.jpg'
        original_image = Image.open(requests.get(original_image_url, stream=True).raw)
        logging.info("Importing Original Image")
        # Download the tampered image
        tampered_image_url = 'https://assets1.cleartax-cdn.com/s/img/20170526124335/Pan4.png'
        tampered_image = Image.open(requests.get(tampered_image_url, stream=True).raw)
        logging.info("Importing tampered Image")
    
        return original_image, tampered_image
    
    except Exception as e:
        raise CustomException(e,sys)


def main():
    # Download images
    original_image, tampered_image = download_images()

    # Perform any further processing or data ingestion tasks here

    # Display the images (optional)
    original_image.show()
    tampered_image.show()

if __name__ == '__main__':
    main()
