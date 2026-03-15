from django.shortcuts import render
from .models import GymAttendance
from datetime import date


def home(request):

    today = date.today()

    if request.method == "POST":

        attendance_value = request.POST.get("attendance")

        went_to_gym = attendance_value == "yes"

        GymAttendance.objects.update_or_create(
            date=today,
            defaults={"went_to_gym": went_to_gym}
        )

    # always executed (GET and POST)
    today_record = GymAttendance.objects.filter(date=today).first()

    total_workouts = GymAttendance.objects.filter(went_to_gym=True).count()

    context = {
        "today_record": today_record,
        "total_workouts": total_workouts,
    }

    return render(request, "tracker/home.html", context)