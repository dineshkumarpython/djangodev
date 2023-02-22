from django.urls import path
# from . import views
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('count', count, name='count'),

]
