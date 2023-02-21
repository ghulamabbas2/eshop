
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_delete

# Create your models here.

class Category(models.TextChoices):
    ELECTRONICS = 'Electronics'
    LAPTOPS = 'Laptops'
    ARTS = 'Arts'
    FOOD = 'Food'
    HOME = 'Home'
    KITCHEN = 'Kitchen'

class Product(models.Model):
    name = models.CharField(max_length=200, default="", blank=False)
    description = models.TextField(max_length=1000, default="", blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    brand = models.CharField(max_length=200, default="", blank=False)
    category = models.CharField(max_length=30, choices=Category.choices)
    ratings = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductImages(models.Model):

    product=models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="images")
    image=models.ImageField(upload_to="products")


@receiver(post_delete, sender = ProductImages)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)


class Review(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)
    comment = models.TextField(default="", blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment)
