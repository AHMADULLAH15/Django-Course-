from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()

    def __str__(self):
        return f"Roll : {self.roll} {self.name}"
    # def __str__(self) -> str:
    #     return super().__str__()+ f"({self.roll})"  # type: ignore