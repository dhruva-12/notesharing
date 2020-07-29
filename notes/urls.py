from django.contrib import admin 
from django.urls import path, include 
from django.conf import settings
from django.conf.urls import static
#from . views import index

  
urlpatterns = [ 
  
    path('admin/', admin.site.urls), 
    
    path('',include('register.urls')),
    #path('register/',include('django.contrib.auth.urls'))
  
   
]
if not settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)