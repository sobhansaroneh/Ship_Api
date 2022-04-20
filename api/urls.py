#from django.conf.urls import url
from django.urls import path, include,re_path
from .views import BookedEvent,RegisterApi,EventView

urlpatterns = [
      path('api/signup' ,RegisterApi.as_view()),
      #path('api/booked', BookedEvent.as_view({'get': 'list'})),
      #path('api/' ,EventView.as_view())

]