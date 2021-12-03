from django.db import models

# Let´s import the Python Models Admin (It´s necessary to create a foreignKey with our tables)
from django.contrib.auth.models import User

# Create your models here.

# Let´s create the event model class
class Event(models.Model):
    
    # Field (attributs)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField(verbose_name="Event Date")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Event Time")
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Here, we´re creating the foreing key with the tabela User. We´re still defining cascanding delete.
    
    # If I want that the table´s name is different the class name:
    class Meta:
        db_table = "event" # event will be the name of table.
        
    # Overload the method str
    def __str__(self):
        return self.title