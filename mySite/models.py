from django.db import models
from django.conf import settings


# Create your models here.
class Reservation(models.model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    numDogs = models.IntegerField()

class Blog(models.model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

class BlogImage(models.model):
    imagePath = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
