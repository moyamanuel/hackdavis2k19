from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "backend/index.html")

def account(request):
    return render(request, "backend/account.html")

def map(request):
    return render(request, "backend/map.html")

def event(request):
    return render(request, "backend/events.html")
