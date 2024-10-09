from django.contrib import admin
from django.urls import path
from App1.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index  , name="index"),
]
