import os.path

from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
from PIL import Image
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

media = 'media'


# Create your views here.

def makepredictions(path):
    # img = Image.open(path)
    img = cv2.imread(path)

    img = cv2.resize(img, (224, 224))  # resize image to match model's expected sizing
    img = img.reshape(1, 224, 224, 3)

    # img_array = np.array(img)
    # img_array = cv2.resize(img_array, (224, 224))

    # img_d = img.resize((224,224))
    #
    #
    # rgb_img = np.array(img,dtype=np.float64)
    # rgb_img = rgb_img.reshape(1,224,224,3)

    # model = keras.models.load_model('model.h5')

    model = keras.models.load_model('model.h5')

    predictions = model.predict(img)
    # a = int(np.argmax(predictions))

    print(predictions)

    return predictions[0][0]


def index(request):
    if request.method == "POST" and request.FILES['upload']:

        if 'upload' not in request.FILES:
            err = 'No images Selected'
            return render(request, 'index.html', {'err': err})
        f = request.FILES['upload']
        if f == '':
            err = 'No images Selected'
            return render(request, 'index.html', {'err': err})
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        prediction = makepredictions(os.path.join(media, file))
        prediction = str(prediction)
        # return render(request, 'index.html', {'pred': prediction, 'file_url': file_url})
        return JsonResponse({'intensity':prediction})
    # return render(request, 'index.html')
    else:
        return render(request, 'index.html')
