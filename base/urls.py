
import statistics
from django import urls
from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.home, name="home"),
    path('index/', views.index, name='index'),
    path('list_view/', views.list_view, name='list_view'),
    path('update_view/<str:pk>', views.update_view, name='update_view'),
    path('delete_view/<str:pk>', views.delete_view, name='delete_view'),
    path('detail_view/<str:pk>', views.detail_view ,name="detail_view"),

    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('bardo1/', views.bardo, name="bardo"),
    path('eljam/', views.eljam, name="eljam"),
    path('carthage/', views.carthage, name="carthage"),
    path('paleochris/', views.paleo, name="paleo"),
    path('city/', views.city, name="city"),
    path('postal/', views.postal, name="postal"),
    path('gallela/', views.gallela, name="gallela"),
    path('atp/', views.atp, name="atp"),

    path('room/<str:pk>/', views.room, name="room"),
    path('room_forum/', views.room_forum, name="room_forum"),
    path('update-room/<str:pk>', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>', views.deleteMessage, name="delete-message"),
    path('list_museums/', views.list, name="list_museums"),
    
    

]
    
    
