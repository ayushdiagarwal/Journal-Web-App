from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Entry(models.Model):
    title = models.CharField(max_length=50, default=timezone.now)
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='Unknown')

    def get_absolute_url(self):
        return reverse('diary:index')

    def __str__(self):
        return self.title
