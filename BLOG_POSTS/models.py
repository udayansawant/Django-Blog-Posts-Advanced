from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    # photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('postlist', args=(str(self.id)))
