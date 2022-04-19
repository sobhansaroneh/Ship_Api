#from django.conf.urls import url
from django.urls import path, include,re_path
from .views import BookedEvent

urlpatterns = [
      path('api/register', BookedEvent.as_view),

]