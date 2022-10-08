from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.TextField()
    user_id = models.BigIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
