from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("My Name , Is Jonny.You are at Polls index")

# Create your views here.
