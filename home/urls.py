from django.urls import path, include
from .views import *

urlpatterns = [
    path('', main),
    path('single/<slug:slug>/', single)
]
