from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
import calendar
import datetime

date = datetime.date.today()
current_date = date.strftime("%d %m %Y")
today = datetime.datetime.strptime(current_date, '%d %m %Y').weekday()
day = calendar.day_name[today]
datei = current_date.replace(' ', '/')
final_date = day[:3] + '. ' + datei


class Entry(models.Model):
    title = models.CharField(max_length=50, default=final_date)
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default='Unknown')

    def get_absolute_url(self):
        return reverse('diary:index')

    def __str__(self):
        return self.title
