
from requests import request
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import EventSerializer, UserSerializer ,BookedEventSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Events , User , Booked
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })



class EventView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Events.objects.all()
    serializer_class = EventSerializer


class BookedEvent(viewsets.ModelViewSet):
    queryset = Booked.objects.all()
    serializer_class = BookedEventSerializer
    
    def post(self , request):
        if request.method == 'POST':
            return Response(' more try')





