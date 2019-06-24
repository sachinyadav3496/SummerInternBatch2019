from django.db import models
from app1.models import AddUser
# Create your models here.
class AddBlog(models.Model):
    author = models.ForeignKey(to=AddUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    post = models.TextField(max_length=100)
    date = models.DateField()
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "{}".format(self.author)
