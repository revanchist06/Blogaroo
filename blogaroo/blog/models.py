from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class BPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "blog_post")
    title = models.CharField(max_length =250)
    slug = models.SlugField(max_length =250)
    body = models.TextField()
    publish = models.DateTimeField(default= timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)

