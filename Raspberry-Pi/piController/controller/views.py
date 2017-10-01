from django.shortcuts import render
from django.http import HttpResponse
from .HVAC import HVAC

unit = HVAC();

def getTemp(request):
    tuple=unit.get_temperature_humidity()
    temp=tuple[1]
    return HttpResponse(str(temp)+" degrees Fahrenheit")

def on(request):
    unit.turn_ac_on()
    return HttpResponse("AC turned ON")

def off(request):
    unit.turn_ac_off()
    return HttpResponse("AC turned OFF")



# Create your views here.
