from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    price = models.FloatField()
    quantity = models.IntegerField()

class Client(models.Model):
    name = models.CharField(max_length=80)
    Address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telephone = models.CharField(max_length=40)

class Order(models.Model):
    class OrderStatus(models.TextChoices):
        IGNORED = "IGNORED"
        CONFIRMED = "CONFIRMED"
        INPROGRESS = "INPROGRESS"
        DELIVERED = "DELIVERED"
        RECEIVED = "RECEIVED"

    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(
        max_length=10,
        choices=OrderStatus.choices,
        default=OrderStatus.CONFIRMED,
    )
    products = models.ManyToManyField(Product)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


    