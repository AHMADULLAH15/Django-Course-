from django.db import models
from author.models import Author
# Create your models here.
class Profiles(models.Model):
    name = models.CharField(max_length=100)
    # email = models.EmailField(max_length=100)
    about = models.TextField()
    # author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='profile')
    author = models.OneToOneField(Author, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.name
    