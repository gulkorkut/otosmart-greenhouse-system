# classification_script.py

import json  # Add import for JSON handling
import logging
import os
import sys

# Set the environment variable to suppress TensorFlow warning
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Add the path to your additional Python packages if needed
# This assumes that your additional packages are inside the 'python_packages' directory
additional_python_packages_path = os.path.join(os.path.dirname(__file__), 'python_packages')
sys.path.append(additional_python_packages_path)

import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions

def load_and_preprocess_image(image_path):
    logging.info(f"Loading and preprocessing image from: {image_path}")

    # Read and decode the image file
    img = tf.io.read_file(image_path)
    img = tf.image.decode_image(img, channels=3)

    # Resize the image to the expected input size of your model
    input_size = (256, 256)  # Adjust based on your model's input size
    img = tf.image.resize(img, input_size)

    # Convert pixel values to the range [0, 1]
    img = tf.image.convert_image_dtype(img, tf.float32)

    # If your model requires further preprocessing, add those steps here

    # Expand dimensions to create a batch of size 1
    img = tf.expand_dims(img, axis=0)

    return img

def load_model(model_path):
    logging.info(f"Loading the model from: {model_path}")
    model = tf.keras.models.load_model(model_path)
    return model

def classify_image(model, image_data):
    logging.info("Classifying image...")
    predictions = model.predict(image_data)
    result = decode_predictions(predictions)

    # Extract class and probability from the result
    top_prediction = result[0][0]
    class_label, class_description, probability = top_prediction

    return {
        'class': class_label,
        'probability': probability
    }

def main(image_path, model_path):
    logging.info(f"Running classification for image: {image_path}")

    # Load the model
    model = load_model(model_path)

    # Load and preprocess the image
    image_data = load_and_preprocess_image(image_path)

    # Perform classification using the loaded model
    result = classify_image(model, image_data)

    # Print or return the result as JSON string
    print(json.dumps(result))

if __name__ == "__main__":
    image_path = sys.argv[1]
    model_path = sys.argv[2]
    main(image_path, model_path)
