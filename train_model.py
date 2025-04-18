import os
import cv2
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 🔹 Fixing the dataset path
IMAGE_FOLDER = r"E:\ANIMAL_PREDICTION 2\ANIMAL_PREDICTION\dataset\images"

# 🔹 Check if the path exists
if not os.path.exists(IMAGE_FOLDER):
    raise FileNotFoundError(f"❌ Path not found: {IMAGE_FOLDER}")

# 🔹 Get all images
images = os.listdir(IMAGE_FOLDER)
if not images:
    raise FileNotFoundError("❌ No images found in dataset/images")

X, y = [], []

for image_name in images:
    img_path = os.path.join(IMAGE_FOLDER, image_name)

    # 🔹 Read the image in grayscale
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"⚠️ Warning: Could not read {image_name}. Skipping.")
        continue  # Skip unreadable files

    # 🔹 Preprocess the image
    img = cv2.resize(img, (64, 64))
    img = img.astype('float32') / 255.0  # Normalize
    img = img.flatten()  # Convert to 1D array

    X.append(img)
    y.append(1 if "dog" in image_name.lower() else 0)  # Label (1=Dog, 0=Cat)

if not X:
    raise ValueError("❌ No valid images found for training!")

# 🔹 Convert to NumPy arrays
X, y = np.array(X), np.array(y)

# 🔹 Split dataset for training (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔹 Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 🔹 Save trained model
joblib.dump(model, 'animal_model.pkl')
print("✅ Model saved as animal_model.pkl")
