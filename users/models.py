from django.db import models

# Create your models here.
class Elder(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Volunteer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

