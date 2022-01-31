from django.db import models
from django.utils import timezone

# Create your models here.
class Vote(models.Model):
    KINOKO = 1
    TAKENOKO = 2

    target = models.IntegerField()
    comment = models.TextField()
    at = models.DateTimeField(default=timezone.now)
