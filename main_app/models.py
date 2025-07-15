from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

INTENSITY_LEVEL = (
    ("1", "Subtle"),
    ("2", "Uncomfortable"),
    ("3", "Moderate"),
    ("4", "Strong"),
    ("5", "Intense"),
)


# Create your models here.
class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=100)
    intensity = models.CharField(max_length=100, choices=INTENSITY_LEVEL)
    journal_text = models.TextField(max_length=250)
    created_at = models.DateField("Journal Date", default=datetime.date.today)

    def __str__(self):
        return f"{self.mood} ({self.id})"

    def get_absolute_url(self):
        return reverse("mood-detail", kwargs={"pk": self.pk})
