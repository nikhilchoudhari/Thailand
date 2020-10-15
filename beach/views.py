from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'beach/home.html')

def mountain(request):
    return render (request, 'beach/mountain.html')

