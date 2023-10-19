from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.handlers.wsgi import WSGIRequest
from .model.FileUpload import FileUpload
from django.core.files.base import File

# Create your views here.
def upload_file(request: WSGIRequest):
    if request.method == "POST":
        form = FileUpload(request.FILES)
        handle_uploaded_file(form.file)
    return HttpResponse("Hello, world. You're at the polls index.")

def handle_uploaded_file(file: File):
    with open(file.name, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
