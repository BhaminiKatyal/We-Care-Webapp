from django.contrib import admin
from django.urls import path, include
from myApp import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('movies', views.movies, name = 'movies'),
    path('quiz', views.quiz, name = 'quiz'),
    path('music', views.music, name = 'music'),
    path('yoga', views.yoga, name = 'yoga'),
    path('doctors', views.doctors, name = 'doctors'),
    path('register/', views.register, name = "register"),
    path('login/', views.login_view, name = "login"),
    path('medicines', views.medicines, name = "medicines"),
    path('videocall', views.videocall, name = "videocall"),
    path('logout', views.logout_view, name = "logout"),
]
