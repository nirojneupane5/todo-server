from django.db import models

# Create your models here.
class Todo(models.Model):
    task_name=models.CharField(max_length=150)
    desc=models.TextField()
    status=models.BooleanField(default=True)