from django.shortcuts import render

# --- Import HttpResponse just to test the views are connecting ---
from django.http import HttpResponse

def index(request):
    return HttpResponse("At the blog index")
