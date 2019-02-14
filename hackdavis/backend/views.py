from django.shortcuts import render
from django.http import HttpResponse
from backend.models import Event
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "backend/index.html")

def create_user(request):
    if request.method == "POST":
        user = User.objects.create_user(
            request.POST.get('email'),
            request.POST.get('email'),
            request.POST.get('password')
    )

    return render(request, "backend/account.html")

def map(request):
    return render(request, "backend/map.html")

def event(request):
    if request.method == "POST":
        new_event = Event(
            event_description = request.POST.get('event_description')
        )
        new_event.save()
    return render(request, "backend/events.html")