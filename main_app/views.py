from django.shortcuts import render, redirect

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')