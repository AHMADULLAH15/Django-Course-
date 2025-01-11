from django.db import models
from a_musician.models import MusicianModel
# Create your models here.
class AlbumModel(models.Model):
    AlbumName = models.CharField(max_length=255)
    musician = models.ForeignKey(MusicianModel,on_delete=models.CASCADE,related_name='albums')
    ReleaseDate = models.DateField()
    value = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating = models.IntegerField(choices=value,default=2)

    def __str__(self):
        return self.AlbumName