from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, request, response

# Create your views here.

def hello_world(request):
    return render(request, "hello.html", {"content": "Just a Basic App"})
