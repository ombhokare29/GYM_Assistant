from django.db import models

# Create your models here.

class GymAttendance(models.Model):
    date = models.DateField(auto_now_add=True)
    went_to_gym = models.BooleanField()
    reason = models.CharField(max_length=200, blank=True)

class Workouts(models.Model):
    date = models.DateField(auto_now_add=True)
    did_workout = models.BooleanField()
    why_not = models.CharField(max_length=500, blank=True)
