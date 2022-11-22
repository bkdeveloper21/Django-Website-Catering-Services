from email import message

from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    mobileno = models.CharField(max_length=255)
    email=models.EmailField(max_length = 254,default='SOME STRING')
    message=models.CharField(max_length=255,default='SOME STRING')  
    


    

    def __str__(self):
        return self.name

class Package(models.Model):
    package_name = models.CharField(max_length=50)
    package_price=models.CharField(max_length=50)
    customer = models.ManyToManyField(Customer)

    

    def __str__(self):
        return self.headline