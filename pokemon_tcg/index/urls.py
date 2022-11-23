from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "index"
urlpatterns = [
    path('', views.index, name='index'),
    path('collection/', views.collection, name='collection'),
    path('exclusive/', views.exclusive, name='exclusive'),
    path('addCard/', views.addCard, name='addCard'),
    path('lookout/', views.lookout, name='lookout'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutPage, name='logout'),
]
