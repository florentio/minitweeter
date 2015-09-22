from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    #Custom user class
    username = models.CharField('username', max_length=255, unique=True, db_index=True)
    email = models.EmailField('email adress', unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'

    def __unicode__(self):
        return self.username
