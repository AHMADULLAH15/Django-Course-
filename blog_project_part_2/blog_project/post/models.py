from django.db import models
from categories.models import Catagory
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # category = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    category = models.ManyToManyField(Catagory) # akta post multiple categorir modde takte pare abr akta categorir modde multiple post takte pare
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title