from dataclasses import field
from multiprocessing import Event
from pyexpat import model
from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import Booked, User , Event


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name' ,'phone_number','email','image')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],     password = validated_data['password']  ,first_name=validated_data['first_name'],  last_name=validated_data['last_name'])
        return user




# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','first_name', 'last_name' ,'phone_number','email','image')



# Event serializer

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('vip','title','totalcapacity', 'capacity' ,
        'date','strattime','endtime','totalprice','currency' ,'music','dinner','drink','transfer' ,'image')



class BookedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booked
        fields = ('user' , 'event' ,'seat')
    def create(self, validated_data):
        return Booked.objects.create(**validated_data)