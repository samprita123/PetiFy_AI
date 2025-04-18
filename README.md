
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
```bash
git clone https://github.com/samprita123/PetiFy_AI.git
cd PetiFy_AI



## Install dependencies:

```Bash
pip install -r requirements.txt

#Run the Flask app:

```Bash
python app.py

#Open browser and go to:
http://localhost:5000

## Upload any cat or dog image and click Predict.
------------------------------------------------------------------------
## Sample pictures of MOdel & Web_page

------------------------------------------------------------------------

## Structure for saving files

PetiFy_AI/
│
├── __MACOSX/
├── _pycache_/
├── dataset/
│   ├── images/
│   ├── input.csv
│   ├── input_test.csv
│   ├── labels.csv
│   └── labels_test.csv
│
├── static/
│   └── uploads/
|   └── script.js
|   └── styles.css
│
├── templates/
│   └── index.html
│
├── animal_model.h5
├── animal_model.pkl
├── app.py
├── train_model.py
├── README.md

