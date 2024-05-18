from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=40)
    roll = models.IntegerField(max_length=10)
    address = models.CharField(max_length=100)
    def __str__(self):
     return f'{self.id}:Name detail {self.name}  Roll detail  {self.roll}  Address detail   {self.address}'