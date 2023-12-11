from django.db import models

class Todo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
