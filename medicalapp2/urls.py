from django.urls import path
from .views import *
urlpatterns = [
    path('', Home, name='home'),
    path('appointment', appointment, name='appointment'),
    path('sample', sample, name='sample'),
]