from flask import Flask, request, render_template
import os
from PIL import Image
from skimage.metrics import structural_similarity
import imutils
import cv2
from src.components.data_processing import data_processing

application = Flask(__name__)

app = application

# Adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/uploads'
app.config['EXISTNG_FILE'] = 'app/original'
app.config['GENERATED_FILE'] = 'app/generated'

# Route to home page
@app.route("/", methods=["GET", "POST"])
def index():
    # Execute if request is GET
    if request.method == "GET":
        return render_template("index.html")

    # Execute if request is POST
    if request.method == "POST":
        # Get uploaded image
        file_upload = request.files['file_upload']
        filename = file_upload.filename

        # Save the uploaded image
        uploaded_image = Image.open(file_upload)
        uploaded_image.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'image.jpg'))

    # Perform data processing
    try:
        ingestion_result, transformation_result = data_processing()
        
        print("Data Ingestion Result:", ingestion_result)
        print("Data Transformation Result:", transformation_result)

        # Return the response to the client
        response = f"Data processing completed. Transformation Result: {transformation_result}"
        return render_template('index.html', pred=response)

    except Exception as e:
        # Handle any errors that occur during data processing
        error_message = "Error occurred during data processing: " + str(e)
        return render_template('index.html', pred=error_message)

# Main function
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)