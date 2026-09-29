from django.urls import path
from . import views

urlpatterns=[
path("",views.home,name="home"),
path("exercises/", views.exercises, name="exercises"),
path("workout/<str:exercise_name>/",views.workout,name="workout"),

]