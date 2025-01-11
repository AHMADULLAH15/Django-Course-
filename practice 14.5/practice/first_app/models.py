from django.db import models
import django.utils.timezone 
# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)
    date_field = models.DateField(default=django.utils.timezone.now)
    date_time_field = models.DateTimeField(default=django.utils.timezone.now)
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2,default=5.5)
    big_integer_field = models.BigIntegerField(default=False)
    # binary_field = models.BinaryField(default=False)
    boolean_field = models.BooleanField(default=False)
    duration_field = models.DurationField(default=False)
    file_field = models.FileField(upload_to='upload/',default=False)
    def __str__(self):
        return f" Name : {self.name} - Email : {self.email}"