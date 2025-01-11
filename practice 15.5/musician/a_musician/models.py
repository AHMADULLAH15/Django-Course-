from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Phone_number = models.IntegerField()
    Instrument_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"