from django.urls import path
from student import student

urlpatterns = [
    path('do/', student.dispatcher),
]
