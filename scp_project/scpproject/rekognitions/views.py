from django.shortcuts import render
from boto.s3.connection import S3Connection
import environ

env = environ.Env()
environ.Env.read_env()

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')

# Create your views here.
def index(request):
    
    # get all images in s3 bucket
    conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    for key in conn.list_objects(Bucket=AWS_STORAGE_BUCKET_NAME)['Contents']:
        context = (key['Key'])
    
    return render(request, 'rekognition/index.html', context)

def show(request, photo):
    # Show Rekognition details of photo
    context = ""
    return render(request, 'rekognition/show.html', context)
