from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User ,Events , Booked

admin.site.register(User)
admin.site.register(Events)
admin.site.register(Booked)