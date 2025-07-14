from django.urls import path
from . import views  # Import views to connect routes to view functions

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path("accounts/signup/", views.signup, name="signup"),
    path('moods/create/', views.MoodCreate.as_view(), name='mood-create'),
]
