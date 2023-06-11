# Pan Card Tampering Detector App

This project is designed to detect tampering or alterations in PAN card images. It compares an original PAN card image with a user-provided image and calculates the Structural Similarity Index (SSIM) to determine the similarity between the two images. If the SSIM score is below a certain threshold, it indicates that the user-provided image may be fake or tampered.

## Requirements

Before running the project, ensure that the following libraries are installed:

-   Pillow
-   requests
-   opencv-python
-   imutils
-   scikit-image

## Getting Started

To run the project, follow these steps:

1.  Create a folder named `pan_card_tampering`.
    
2.  Inside the `pan_card_tampering` folder, create another folder named `image`.
    
4.  Run the notebook cells to perform the following tasks:
    
    -   Import the necessary libraries.
    -   Download and display the original and tampered PAN card images.
    -   Convert the tampered image format to match the original image format.
    -   Resize both images to the desired dimensions.
    -   Convert the images to grayscale.
    -   Calculate the SSIM score between the images.
    -   Apply thresholding and contour detection on the difference image.
    -   Draw bounding rectangles around the detected contours.
    -   Display the original image, tampered image, difference image, and threshold image.
5.  Based on the displayed results, you can determine if the user-provided image is tampered or not.
    

## Project Structure

The project has the following structure:
```plaintext 
`.
├── app/uploads
├── artifacts
│  ├── transformed
├── cenv
├── notebook
│  ├── Pan_Card_Tampering.ipynb
├── src
│   ├── components
│   ├──data_ingestion.py
│   ├──data_processing.py
│   ├──data_transformation.py
├── __init__.py
├── exception.py
├── logger.py
├── utils.py
├── templates
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py` 
```

-   `app/uploads/`: This directory is used for storing uploaded images.
-   `artifacts/`: This directory is used for storing deployment artifacts.
    -   `transformed/`: This subdirectory might contain transformed or processed data files or artifacts.
-   `cenv/`: This directory is used for virtual environment files. It is typically created during the deployment process.
-   `notebook/`: This directory is used for storing Jupyter notebooks, including the main detection notebook (`Pan_Card_Tampering.ipynb`).
-   `src/`: This directory contains the source code files.
    -   `components/`: This subdirectory might contain specific components or modules related to the project.
    -   `data_ingestion.py`: This file is responsible for handling data ingestion, such as loading data from a source.
    -   `data_processing.py`: This file is responsible for data processing tasks, such as cleaning or transforming data.
    -   `data_transformation.py`: This file is responsible for data transformation tasks, such as converting data to a different format.
-   `__init__.py`: This is an empty initialization file, typically used to mark a directory as a Python package.
-   `exception.py`: This file contains code related to handling exceptions and errors.
-   `logger.py`: This file contains code related to logging events and messages.
-   `utils.py`: This file contains utility functions that are used in the project.
-   `templates/`: This directory contains HTML templates for the web app.
-   `.gitignore`: This file specifies which files and directories should be ignored by version control (e.g., Git).
-   `README.md`: This file contains instructions and information about the project.
-   `requirements.txt`: This file lists the required Python packages and their versions.
-   `setup.py`: This file is a configuration file for project setup and might contain instructions for installing dependencies or setting up the project environment.

## Deployment

This project can be deployed on a web server or cloud platform.
![Screenshot (94)](https://github.com/pras-ops/Card_Tampering/assets/56476064/05084e69-5831-48f9-b317-669f16009b56)


