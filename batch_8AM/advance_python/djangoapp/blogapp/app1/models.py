from django.db import models

# Create your models here.
class AddUser(models.Model):
    Email = models.EmailField(unique=True)
    Username = models.CharField(max_length=50,default=None)
    Password = models.CharField(max_length=40)
    Profile = models.ImageField()
    Active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.Email)
