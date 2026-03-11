from django.contrib import admin

# Register your models here.

from .models import GymAttendance,Workouts
admin.site.register(GymAttendance)
admin.site.register(Workouts)

