from django.shortcuts import render

# Create your views here.
def chord_quality(request):
    return render(request, 'ear_training/chord_quality.html')


def help(request):
    return render(request, 'ear_training/help.html')