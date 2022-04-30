from django.shortcuts import render

import environ

env = environ.Env()
environ.Env.read_env()

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')

# Create your views here.
def index(request):
    
    # get all images in s3 bucket
    
    return render(request, 'rekognition/index.html')

def show(request, photo):
    # Show Rekognition details of photo
    context = ""
    return render(request, 'rekognition/show.html', context)
