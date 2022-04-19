from locale import currency
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser ,User
#from phonenumber_field.modelfields import PhoneNumberField



class User(AbstractUser):
    # firstname= models.CharField(max_length=30)
    # lastname= models.CharField(max_length=30)
    phone_number = models.PositiveBigIntegerField(null=True,blank=True, help_text='Contact phone number')
    email = models.EmailField(blank=True,null=True)
    password = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'files/profile_img',null=True, blank=True)

    def __str__(self) -> str:
        return self.username


class Events(models.Model):
    currency= (
    ("USD", "USD"),
    ("TRY", "TRY"),
    )
    vip = models.BooleanField()
    title = models.CharField(max_length=20)
    totalcapacity = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    date = models.DateField()
    strattime = models.TimeField()
    endtime = models.TimeField()
    totalprice = models.PositiveIntegerField()
    currency= models.CharField(choices=currency, max_length=20)
    music = models.BooleanField()
    dinner = models.BooleanField()
    transfer = models.BooleanField()
    drink = models.BooleanField()
    def __str__(self) -> str:
        return self.title
    


class Booked(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    event = models.ForeignKey(Events,on_delete=models.CASCADE)
    seat = models.PositiveIntegerField()


    def __str__(self) -> str:
        return f'{self.user}'
    