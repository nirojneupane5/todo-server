from django.db import models

# Create your models here.
class Todo(models.Model):
    task_name=models.CharField(max_length=150,)
    desc=models.CharField()
    status=models.BooleanField(default=False)