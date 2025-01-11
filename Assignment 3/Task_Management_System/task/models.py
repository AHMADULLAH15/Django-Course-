from django.db import models
from category.models import CategoryModel
# Create your models here.
class TaskModel(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=250)
    task_description = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField()
    categories = models.ManyToManyField(CategoryModel)

    def __str__(self):
        # return super().__str__()+ self.task_title
        return f"{self.task_title}"