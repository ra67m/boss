from django.urls import path,re_path
from myApp import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('home/page/<num>/',views.home,name='home'),
    path('logOut/',views.logOut,name='logOut'),
    path('center/',views.center,name='center'),
    path('jianli/',views.jianli,name='jianli')
]