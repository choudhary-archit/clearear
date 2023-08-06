from django.shortcuts import render


def home(request):
    return render(request, 'ear_training/train_home.html')


def help(request):
    return render(request, 'ear_training/help.html')


def chord_quality(request):
    return render(request, 'ear_training/chord_quality.html')


def rhythmic_dictation(request):
    return render(request, 'ear_training/rhythmic_dictation.html')