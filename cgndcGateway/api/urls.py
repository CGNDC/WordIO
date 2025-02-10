from django.urls import path
from . import views

urlpatterns = [
    path('db/', views.ping_db, name='ping_db'),
    path('ml/', views.ping_ml, name='ping_ml'),
]