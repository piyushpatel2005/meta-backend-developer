from django.urls import path

import myapp.views as views

urlpatterns = [
    path('drinks/<str:drink_name>', views.drinks, name="drinks"),
]