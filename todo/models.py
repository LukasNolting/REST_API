from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Todo(models.Model):
    Title = models.CharField(max_length=30)
    Description = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    user = models.ForeignKey(
                        User, 
                        on_delete=models.CASCADE,
                        default=None
                        )
