from django.db import models


class Bikes(models.Model):
    
    bike_name = models.CharField(max_length=100)
    bike_decription = models.TextField()
    bike_image = models.ImageField(upload_to='bikes' ,default='default.jpg')
    
    
