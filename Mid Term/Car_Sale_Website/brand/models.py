from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank=True,null=True)

    def __str__(self):
        return self.name
