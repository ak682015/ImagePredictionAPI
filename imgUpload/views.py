from django.shortcuts import render
from .forms import ImageUploadForm
from . import prediction
import numpy as np

def handle_uploaded_file(f):
    with open('userimages/img.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def home(request):
    return render(request, 'imgUpload/home.html')


def imageprocess(request):
    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
        handle_uploaded_file(request.FILES['image'])
        # img_path = 'userimages/img.jpg'
        output = prediction.find()
        return render(request, 'imgUpload/result.html', {'res': output})

    return render(request, 'imgUpload/result.html')
