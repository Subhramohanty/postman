from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=64)
    phone=models.CharField(max_length=20,blank=True,null=True)

class Product(models.Model):
    product_name=models.CharField(max_length=64)

class Category(models.Model):
    category_name= models.CharField(max_length=200,default=1)
    
class Order(models.Model):
    product_id=models.CharField(max_length=20)
    category_id=models.CharField(max_length=20)
    price=models.CharField(max_length=100)
    email = models.EmailField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

def __str__(self):
    return self.name
    
        
