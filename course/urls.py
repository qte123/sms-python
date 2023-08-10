from django.urls import path
from course import course

urlpatterns = [
    path('do/', course.dispatcher)
]
