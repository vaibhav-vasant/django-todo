from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        if len(self.password) > 10:
            self.password = self.password[:10]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
