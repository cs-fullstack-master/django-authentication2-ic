
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_classes, name='allclasses'),
    path('myclasses/', views.my_classes, name='myclasses'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]