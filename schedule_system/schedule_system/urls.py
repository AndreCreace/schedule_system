"""schedule_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Let´s import the views
from core import views 

# Let´s import the library to redirect pages
from django.views.generic import RedirectView

# Let´s define the routes
urlpatterns = [
    path('', RedirectView.as_view(url='/schedule/')),  # Index Site Page (Let´s redirect to schedule page)
    path('schedule/', views.list_user_events),              # Schedule
    path('admin/', admin.site.urls),                   # Admin
    path('login/', views.login_user),                  # Login page
    path('login/submit', views.submit_login),          # Validade User and Password
    path('logout/', views.logout_user)
]
