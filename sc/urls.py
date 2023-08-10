from django.urls import path
from sc import sc, gradeSelect

urlpatterns = [
    path('do/', sc.dispatcher),
    path('select/', gradeSelect.dispatcher)
]
