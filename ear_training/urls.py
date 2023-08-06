from django.urls import path
from . import views


app_name = 'ear_training'
urlpatterns = [
    path('chord_quality/', views.chord_quality, name='chord_quality'),
    path('help/', views.help, name='help')
]