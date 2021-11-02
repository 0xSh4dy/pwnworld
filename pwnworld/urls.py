
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('stuff.urls')),
    path('tools/',include('tools.urls'))
]
