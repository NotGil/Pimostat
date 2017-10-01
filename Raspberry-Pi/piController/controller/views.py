from django.shortcuts import render
from django.http import HttpResponse

def getTemp(request):
    return HttpResponse("78 degrees cause why not")

def on(request):
    return HttpResponse("AC turned ON")

def off(request):
    return HttpResponse("AC turned OFF")



# Create your views here.
