from django.shortcuts import render, HttpResponse, redirect

# Let´s import the model
from core.models import Event

# Create your views here.

# Function to show Index Site Page
#def index(request):
   #return redirect('/agenda/')

# Function to show the schedules
def list_events(request):
    
    # Let´s take the user who submetted the request (User with session active)
    #userRequest = request.user
    
    # Let´s full query on event table
    events = Event.objects.all()
    
    # Let´s filter some the user request events
    #events = Event.objects.filter(user = userRequest)
    
    # Let´s define the response
    data = {"events" : events}
    
    # Function returns
    return render(request,"schedule.html", data)