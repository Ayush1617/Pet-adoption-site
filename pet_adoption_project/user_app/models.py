from django.db import models
from django.contrib.auth.models import User



class user_details(models.Model):
    username = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    email= models.EmailField()
    password = models.CharField(max_length=100)
    user_age = models.IntegerField()
    user_image=models.ImageField(upload_to='user_images/',null=True,blank=True)
    def __str__(self):
        return( self.username)
    


class adoption_application(models.Model):
    username = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    email= models.EmailField()
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


    