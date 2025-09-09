from django.contrib import admin
from django.urls import path, include
from .views import *
app_name = 'app'
urlpatterns = [
    path('home2/', home2, name='home2')

]
