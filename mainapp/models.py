from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Furniture(models.Model):
    STYLE_CHOICES = [
        ('modern', 'ソファ'),
        ('classic', '机'),
        ('industrial', '椅子'),
        ('scandinavian', 'ランプ'),
        ('bohemian', 'その他'),
    ]

    name = models.CharField(max_length=100)
    height = models.IntegerField()
    width = models.IntegerField()
    depth = models.IntegerField()
    style = models.CharField(max_length=50, choices=STYLE_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='furniture_images/', null=True, blank=True)

    def __str__(self):
        return self.name
class RoomPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='room_photos/')
    