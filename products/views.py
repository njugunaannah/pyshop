from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def index(request):
    return HttpResponse("testing")


def new(request):
    return HttpResponse("new product")
