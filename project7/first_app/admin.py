from django.contrib import admin
# from first_app.models import StudentModel
# from .models import StudentModel
from . import models
# Register your models here.
admin.site.register(models.StudentModel)

# username admin email admin@gmail.com pass 1234