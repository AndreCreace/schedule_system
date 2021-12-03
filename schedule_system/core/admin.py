from django.contrib import admin

# Let´s import the models
from core.models import Event

# Let´s define, wich Event fiels will be displayed
class EventAdmin(admin.ModelAdmin):
    
    # Let´s define the fields
    list_display = ("title", "event_date", "created_at")
    
    # Let´s create and define wich Event fields, the user can to search.
    list_filter = ("title", "event_date")

# Register your models here.
admin.site.register(Event, EventAdmin)