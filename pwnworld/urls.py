
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('stuff.urls')),
    path('challenges/',include('challenges.urls'))
]
