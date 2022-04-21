from itertools import count
from locale import currency
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser ,User
#from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import Count ,Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    # firstname= models.CharField(max_length=30)
    # lastname= models.CharField(max_length=30)
    phone_number = models.PositiveBigIntegerField(null=True,blank=True, help_text='Contact phone number')
    email = models.EmailField(blank=True,null=True)
    password = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'files/profile_img',null=True, blank=True)

    def __str__(self) -> str:
        return self.username


class Event(models.Model):
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
    image = models.ImageField(upload_to ='files/event_img')
    music = models.BooleanField()
    dinner = models.BooleanField()
    transfer = models.BooleanField()
    drink = models.BooleanField()
    def __str__(self) -> str:
        return str(self.date)
    


class Booked(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='Booked')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='Booked')
    seat = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return f'{self.event}'
    


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Booked)
def booking(sender , instance , created ,**kwarg):
    if created:
        event_q = Event.objects.get(date = str(instance.event))
        event_q.capacity = + instance.seat
        event_q.save()
        