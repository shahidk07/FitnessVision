from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")


def exercises(request):
    return render(request, "exercises.html")

def workout(request,exercise_name):
    return render(request,"workout.html",
                  {
                      "exercise":exercise_name
                  })