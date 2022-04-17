from django.db import models
from django.contrib.auth.models import AbstractUser ,User
#from phonenumber_field.modelfields import PhoneNumberField



class User(AbstractUser):
    # firstname= models.CharField(max_length=30)
    # lastname= models.CharField(max_length=30)
    phone_number = models.PositiveBigIntegerField(blank=True, help_text='Contact phone number')
    email = models.EmailField(blank=True,null=True)
    password = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'files/profile_img',null=True, blank=True)

    def __str__(self) -> str:
        return self.email
