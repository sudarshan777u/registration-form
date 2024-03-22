from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=100)
    highest_qualification=models.CharField(max_length=200)
    percentage=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    year_of_passing=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    certifications=models.FileField()
    skills=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
