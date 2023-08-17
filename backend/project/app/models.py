from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

class Address(models.Model):
    city = models.CharField(max_length=100)
    downtown = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class ShopOrder(models.Model):
    code = models.CharField(max_length=100)
    total_amount = models.CharField(max_length=100)
    pay_method = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    identifier = models.CharField(max_length=100)
    shopOrder = models.ManyToManyField(ShopOrder)

class Variation(models.Model):
    price = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

