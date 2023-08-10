from django.urls import path
from app import go

urlpatterns = [
    path('', go.go_login),
]
