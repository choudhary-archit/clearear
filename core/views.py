from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def login_view(request):
    pass


def signup_view(request):
    pass


def dashboard(request):
    pass


def logout_view(request):
    pass