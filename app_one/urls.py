from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('getGold',views.collectGold),
    path('postGold',views.return_gold),
]