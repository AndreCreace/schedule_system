from django.shortcuts import render, HttpResponse, redirect

# Let´s import the model
from core.models import Event

# Let´s import library to authenticate users
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Let´s import the library to work error messages
from django.contrib import messages

# Function to redirect unauthenticated user
def login_user(request):
       
   # Let´s render
   return render(request, 'login.html')

# Function to validade User/Password (POST)
def submit_login(request):
       
   # If POST
   if request.POST:
          
      # Let´s recive the values from form login
      userName = request.POST.get("username")
      userPassword = request.POST.get("password")
      
      # Let´s validate the user/login
      userAuthenticated = authenticate(username=userName, password=userPassword)
      
      if userAuthenticated is not None:
         login(request, userAuthenticated)
         return redirect("/")
      else:
         messages.error(request, "Invalid username ou password!!!")

   # Function returns
   return redirect("/")
   
# Funtions logout
def logout_user(request):
       
   # Let´s clean the session
   logout(request)
   
   # Let´s redirect to index
   return redirect("/")
          
# Function to show the schedules. Let´s input the decorator to autenticate user
@login_required(login_url="/login/")
def list_user_events(request):    
    
    # Let´s full query on event table
    #events = Event.objects.all() 
    
    # Let´s filter the user schedules
    events = Event.objects.filter(user=request.user)
    
    # Let´s define the response
    data = {"events" : events}
    
    # Function returns
    return render(request,"schedule.html", data)
 
# Function to show Index Site Page
#def index(request):
   #return redirect('/agenda/')