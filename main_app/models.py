from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

INTENSITY_LEVEL = (
    ("1", "Subtle"),
    ("2", "Mild"),
    ("3", "Moderate"),
    ("4", "Strong"),
    ("5", "Intense"),
)

MOOD_CHOICES = [
    ("Happy", "Happy 😊"),
    ("Sad", "Sad 😢"),
    ("Angry", "Angry 😠"),
    ("Anxious", "Anxious 😰"),
    ("Calm", "Calm 😌"),
    ("Excited", "Excited 🤩"),
    ("Tired", "Tired 😴"),
    ("Grateful", "Grateful 🙏"),
    ("Other", "Other ✍️"),
]


# Create your models here.
class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=100, choices=MOOD_CHOICES)
    intensity = models.CharField(max_length=100, choices=INTENSITY_LEVEL)
    journal_text = models.TextField(max_length=250)
    affirmation = models.TextField(blank=True, null=True)
    created_at = models.DateField("Journal Date", default=datetime.date.today)

    def __str__(self):
        return f"{self.mood} ({self.id})"

    def get_absolute_url(self):
        return reverse("mood-detail", kwargs={"pk": self.pk})

# class GeneratedAffirmation(models.Model):
#     """Store generated affirmations linked to mood entries"""
#     mood_entry = models.OneToOneField(MoodEntry, on_delete=models.CASCADE, related_name='affirmation')
#     affirmation_text = models.TextField()
#     generated_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"Affirmation for {self.mood_entry.mood}"