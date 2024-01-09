from django.db import models
from django.conf import settings


# Create your models here.
class Reservation(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    numDogs = models.IntegerField()

    def __str__(self):
        return f"{self.startDate} to {self.endDate}"

class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class BlogImage(models.Model):
    imagePath = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.imagePath
