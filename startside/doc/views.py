from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def doc_home(request):
    return HttpResponse("Home Page")