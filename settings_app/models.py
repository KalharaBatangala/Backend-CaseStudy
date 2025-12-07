from django.db import models

class AccountSettings(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # will store hashed password
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
