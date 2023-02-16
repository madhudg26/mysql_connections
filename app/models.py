from django.db import models

# Create your models here.


class Student(models.Model):
    SID=models.IntegerField(primary_key=True)
    NAME=models.CharField(max_length=100)
    AGE=models.IntegerField()