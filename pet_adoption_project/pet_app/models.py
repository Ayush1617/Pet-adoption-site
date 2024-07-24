from django.db import models

class pet_details(models.Model):
    pet_name = models.CharField(max_length=100)
    about_pet= models.TextField(max_length=200)
    pet_type = models.CharField(max_length=100)
    pet_age = models.IntegerField()
    pet_breed = models.CharField(max_length=100)
    pet_image=models.ImageField(upload_to='pet_images/',null=True,blank=True)
    class meta:
        name = 'pet_details'

    def __str__(self):
        return( self.pet_name)
    