from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("this is vicky page")
def about(request):
    return HttpResponse("this is about page")