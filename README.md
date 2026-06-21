# Digit Recognition System

A Deep Learning web application that recognizes handwritten digits from uploaded images using TensorFlow and Django.

## Project Overview

This project demonstrates the complete Machine Learning workflow from model training to deployment. Users can upload an image containing a handwritten digit, and the system predicts the digit with a confidence score using a trained neural network model.

The application combines Deep Learning, Computer Vision, and Web Development into a single end-to-end solution.

---

## Features

* Handwritten digit recognition
* Real-time prediction
* Confidence score display
* Image upload and preview
* Responsive modern user interface
* TensorFlow-powered inference
* Django web deployment

---

## Technologies Used

### Machine Learning

* TensorFlow
* Keras
* NumPy

### Backend

* Python
* Django

### Frontend

* HTML
* Tailwind CSS
* JavaScript

### Dataset

* MNIST Handwritten Digits Dataset

---

## Machine Learning Pipeline

1. Load and preprocess MNIST dataset
2. Normalize image pixel values
3. Train Deep Learning model
4. Save trained model
5. Deploy model with Django
6. Accept image uploads
7. Perform inference
8. Display prediction and confidence score

---

## Project Structure

```text
DigitRecognizer/
├── DigitRecognizer/
├── predictor/
├── templates/
├── media/
├── manage.py
├── requirements.txt
├── mnist_model.h5
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Prajapati-Harsh-224/digit-recognition-system.git
```

Move into the project directory:

```bash
cd digit-recognition-system
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Django server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Future Improvements

* Draw digit directly on canvas
* Support custom datasets
* Prediction history
* Model performance dashboard
* Docker deployment
* Cloud deployment

---

## Author

**Harsh Prajapati**

LinkedIn:
https://www.linkedin.com/in/harsh-prajapati-5119a02ba/

GitHub:
https://github.com/Prajapati-Harsh-224
