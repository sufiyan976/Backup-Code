from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# basic
class usermodel1(models.Model):
    name = models.CharField(max_length=20 ,null=False)
    email1 = models.CharField(max_length=20 ,null=False)
    message = models.CharField(max_length=500 ,null=False)
    def __str__(self):
         return self.name

# if request.user is always anonymous then use this model
# also create create another file named backends.py in your app for (AbstractBaseUser)
# also dont forget to use (from django.contrib.auth.models import AbstractBaseUser)
class usermodel(AbstractBaseUser):
    username = models.CharField(max_length=20 ,null=False)

    email = models.CharField(max_length=20 ,null=False)
    password = models.CharField(max_length=12 ,null=False)
    confirmpassword = models.CharField(max_length=12 ,null=False)
    # timestamp = models.DateField(auto_now_add=True,auto_now=False,blank=True)

    def __str__(self):
        return self.username


    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    