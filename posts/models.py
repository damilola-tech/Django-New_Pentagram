from django.db import models

# Create your models here.
from users.models import User


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/posts')