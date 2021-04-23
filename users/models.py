from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=15)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to="gallery/users")
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
