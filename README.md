
# Petify AI

*Petify AI* is an AI-powered image classification model that predicts whether an uploaded image is of a *Cat* or a *Dog*.

---

## Project Details

- The model uses a Convolutional Neural Network (CNN) built using TensorFlow/Keras.
- It accepts an image input from the user through a simple web interface.
- After processing, it displays whether the image is a cat or a dog.

---

## Technical Stack

- Python  
- TensorFlow / Keras  
- Flask  
- HTML, CSS (for frontend)  
- Jupyter Notebook (for training)

---

## How to Use

1. Clone the repository:
bash
git clone https://github.com/samprita123/PetiFy_AI.git
cd PetiFy_AI


2. Install Dependencies:
bash
pip install -r requirements.txt


3. Run the Flask app:
bash
python app.py


4. Open browser and go to:

http://localhost:5000


5. Upload any cat or dog image and click *Predict*.
------------------------------------------------------------------------
## Sample pictures of MOdel & Web_page
![Model Prediction](https://github.com/samprita123/Petify_AI/blob/main/Screenshot%202025-04-15%20193328.png?raw=true)
![Running Page](https://github.com/samprita123/Petify_AI/blob/main/Screenshot%202025-04-15%20205149.png?raw=true)

------------------------------------------------------------------------

## Structure for saving files


PetiFy_AI/
├── __MACOSX/

├── __pycache__/

├── dataset/
│   ├── images/
│   ├── input.csv
│   ├── input_test.csv
│   ├── labels.csv
│   └── labels_test.csv
│

├── static/
│   ├── uploads/
│   ├── script.js
│   └── styles.css
│

├── templates/
│   └── index.html
│

├── animal_model.h5

├── animal_model.pkl

├── app.py

├── train_model.py

└── README.md


