from flask import Flask, render_template, request, jsonify
import os
import random
import cv2
import numpy as np
import joblib

# Flask app setup
app = Flask(__name__, template_folder="templates", static_folder="static")
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Model path
MODEL_PATH = os.path.join('animal_model.pkl')
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Model file '{MODEL_PATH}' not found!")

model = joblib.load(MODEL_PATH)

# Dataset folder (use your full path)
IMAGE_FOLDER = r"E:\ANIMAL_PREDICTION 2\ANIMAL_PREDICTION\dataset\images"
if not os.path.exists(IMAGE_FOLDER):
    raise FileNotFoundError(f"❌ Dataset folder '{IMAGE_FOLDER}' not found!")

images = os.listdir(IMAGE_FOLDER)

def preprocess_image(image_path):
    """Preprocess image for model prediction."""
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (64, 64))
    img = img.astype('float32') / 255.0
    img = img.flatten().reshape(1, -1)
    return img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        img = preprocess_image(file_path)
        pred = model.predict(img)
        label = 'Dog' if pred[0] == 1 else 'Cat'

        return jsonify({
            'image': file.filename,
            'prediction': label,
            'file_path': file_path
        })

    # GET request: Random image from dataset
    if not images:
        return jsonify({"error": "No images in dataset folder!"}), 500

    image_name = random.choice(images)
    image_path = os.path.join(IMAGE_FOLDER, image_name)

    img = preprocess_image(image_path)
    pred = model.predict(img)
    label = 'Dog' if pred[0] == 1 else 'Cat'

    return jsonify({
        'image': image_name,
        'prediction': label
    })

if __name__ == '__main__':
    app.run(debug=True)
