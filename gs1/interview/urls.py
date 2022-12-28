from django.urls import path,include
from . import views

urlpatterns = [
    path('interview/',views.Divvy_Bikes.as_view()),
]