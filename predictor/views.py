import os
import numpy as np
import tensorflow as tf
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from PIL import Image

# Load the MNIST model once when Django starts.
MODEL_PATH = os.path.join(settings.BASE_DIR, 'model.mnist.h5')
model = tf.keras.models.load_model(MODEL_PATH)

# Supported image file extensions.
ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg'}


def is_allowed_file(filename):
    _, ext = os.path.splitext(filename.lower())
    return ext in ALLOWED_EXTENSIONS


def preprocess_image(image_path):
    """Open the uploaded image, convert to grayscale, resize, normalize, and reshape."""
    with Image.open(image_path) as image:
        image = image.convert('L')
        image = image.resize((28, 28))
        image_array = np.asarray(image).astype('float32')
        image_array = image_array / 255.0
        image_array = image_array.reshape(1, 784)
    return image_array


def index(request):
    context = {
        'prediction': None,
        'confidence': None,
        'uploaded_image_url': None,
        'error': None,
    }

    if request.method == 'POST' and request.FILES.get('digit_image'):
        uploaded_file = request.FILES['digit_image']
        if not is_allowed_file(uploaded_file.name):
            context['error'] = 'Please upload a PNG, JPG, or JPEG file.'
            return render(request, 'index.html', context)

        upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
        os.makedirs(upload_dir, exist_ok=True)
        fs = FileSystemStorage(location=upload_dir)
        filename = fs.save(uploaded_file.name, uploaded_file)
        saved_path = fs.path(filename)
        context['uploaded_image_url'] = f"{settings.MEDIA_URL}uploads/{filename}"

        try:
            image_data = preprocess_image(saved_path)
            predictions = model.predict(image_data, verbose=0)
            predicted_digit = int(np.argmax(predictions, axis=1)[0])
            confidence_score = float(np.max(predictions, axis=1)[0])

            context['prediction'] = predicted_digit
            context['confidence'] = f'{confidence_score * 100:.2f}%'
        except Exception as exc:
            context['error'] = f'Error processing image: {exc}'

    return render(request, 'index.html', context)
