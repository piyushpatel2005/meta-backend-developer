from django.urls import path

import myapp.views as views

urlpatterns = [
    path('', views.home, name="home"),
    path('aboutus/', views.about, name="aboutus"),
    path('menu/', views.menu, name="menu"),
    path('book/', views.book, name="book"),
]