from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    
    
    def __str__(self):
        return str(self.username)
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=6, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.IntegerField(blank=True, null=True)
    
    
    def __str__(self):
        return str(self.email)