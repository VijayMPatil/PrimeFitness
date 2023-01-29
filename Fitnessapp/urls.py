from django.urls import path
from .views import signup,handlelogin,home,handlelogout,handlecontact,enroll,getprofile,getattendance,gallery,getservices,about

urlpatterns = [
    path('',home),
    path('signup',signup),
    path('login',handlelogin),
    path('logout',handlelogout),
    path('contact',handlecontact),
    path('join',enroll),
    path('profile',getprofile),
    path('attendance',getattendance),
    path('gallery',gallery),
    path('about',about),
    path('services',getservices),

]
