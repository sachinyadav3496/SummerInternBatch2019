from django.db import models

# Create your models here.
class AddUser(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=40)
    pic = models.ImageField(upload_to="static/images")

    def __str__(self):
        return "{}".format(self.email)
