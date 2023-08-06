from django.urls import path
from . import views


app_name = 'ear_training'
urlpatterns = [
    path('', views.home, name='home'),
    path('help/', views.help, name='help'),
    path('chord_quality/', views.chord_quality, name='chord_quality'),
    path('rhythmic_dictation/', views.rhythmic_dictation, name='rhythmic_dictation'),
]