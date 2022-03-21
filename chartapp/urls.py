from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('databoard/', views.databoard, name='databoard'),
]
