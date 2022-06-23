import email
from django.db import models

class users(models.Model):
    
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    emailid = models.EmailField()
    userid = models.IntegerField()
    salry = models.IntegerField()
    
    def __str__(self):
        return self.firstname
    



# Create your models here.
