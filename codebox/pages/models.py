from django.db import models
from django.urls import reverse

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    query = models.TextField()

    def __str__(self):
        return "{}-{}".format("mail from",self.email)

    def get_absolute_url(self):
        return reverse('about')
