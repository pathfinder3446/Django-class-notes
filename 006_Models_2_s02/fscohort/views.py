from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome Backend')

def fscohort(request):
    return HttpResponse('You are in fscohort now')

def subfolder(request):
    return HttpResponse('Now, you are in subfolder')