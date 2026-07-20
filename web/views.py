from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponse("Contact")

