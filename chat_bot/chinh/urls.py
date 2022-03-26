from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/<int:idu>/', views.chat, name='chat'),
    path('ad/signin/', views.ad_signin, name='ad_signin'),
]