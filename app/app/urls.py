from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls, name='index'),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog'))
    
]
