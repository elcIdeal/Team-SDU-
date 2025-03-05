from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=100, unique=True)
    balance = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
