from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booked , Events


@receiver(post_save, sender=Booked)
def booking(sender , instance , created ,**kwarg):
    if created:
        print('///////////')
        cap=Events.capacity
        ins=instance.seat
        Events.capacity =cap - ins
        print(Events.capacity)
        return True


