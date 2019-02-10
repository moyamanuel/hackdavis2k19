from django.shortcuts import render
from django.http import HttpResponse
from backend.models import Event

# Create your views here.
def index(request):
    if request.method == "POST":
        new_event = Event(
            image_link= request.POST.get('image_link'),
            event_address= request.POST.get('event_address'),
            importance_rank= request.POST.get('importance_name'),
            event_description=request.POST.get('event_description')
        )
        new_event.save()
    return render(request, "backend/index.html")

def create(request):
    return render(request, "backend/account.html")