from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name 
    
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    
    def __str__(self):
        return self.user 
    
class Users(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    companyname = models.CharField(max_length=100)
    email = models.EmailField()
    addressline1 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.companyname