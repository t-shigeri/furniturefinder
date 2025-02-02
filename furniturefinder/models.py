from django.db import models

class Furniture(models.Model):
    name = models.CharField(max_length=100)
    height = models.FloatField()
    width = models.FloatField()
    depth = models.FloatField()
    style = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='furniture_images/')