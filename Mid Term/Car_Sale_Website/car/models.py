from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User
# Create your models here.
class Car(models.Model):
    name = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField(max_length=1000)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    image = models.ImageField(upload_to='car/media/uploads/')
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    purchased_cars = models.ManyToManyField(Car,blank=True)

    def __str__(self):
        return self.user.username
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    comment = models.TextField(max_length=1000)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment By {self.name}"