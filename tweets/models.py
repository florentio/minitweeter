from django.db import models
from user_profile.models import User

# Create your models here.

class Tweet(models.Model):
#tweet Model
    user = models.ForeignKey(User)
    text = models.CharField(max_length=160)
    created_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=16)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.text

class HashTag(models.Model):
#Hashtag Model
    name = models.CharField(max_length=64, unique=True)
    tweets = models.ManyToManyField(Tweet)

    def __unicode__(self):
        return self.name
