import requests
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import CreateView
from .models import MoodEntry



class Home(LoginView):
    template_name = "home.html"

class MoodCreate(CreateView):
    model = MoodEntry
    fields = '__all__'
    success_url = '/about/'

def moods_index(request):
  moods = MoodEntry.objects.all()
  return render(request, 'moods/index.html', {'moods': moods})

def about(request):
    return render(request, "about.html")


def signup(request):
    error_message = ""
    if request.method == "POST":
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect("about")
        else:
            error_message = "Invalid sign up - try again"
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)


def mood_detail(request, pk):
    mood = MoodEntry.objects.get(id=pk)
    return render(request, 'moods/detail.html', {'mood': mood})