from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.IntegerField()
    job = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
