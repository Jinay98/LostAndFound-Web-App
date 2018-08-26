from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    UID = models.IntegerField(default=0)
    branch = models.CharField(max_length=20, default='Computer')
    year = models.CharField(max_length=20, default='First year')
    contactno = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

class ItemData(models.Model):
    ItemID = models.AutoField(primary_key=True)
    Description = models.CharField(default="",max_length=150)
    Location = models.CharField(default="",max_length=100)
    Image = models.ImageField()
    Find_Date = models.DateTimeField(auto_now=True)

