from django.db import models

# Create your models here.
class stu_reg(models.Model):
    name=models.CharField()
    email=models.EmailField()
    number=models.CharField()
    dob=models.DateField()
    gender=models.CharField()
    username=models.CharField()
    password=models.CharField()
    address=models.CharField()
    country=models.CharField()
    agree=models.CharField()