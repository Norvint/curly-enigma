from django.contrib import admin
from django.urls import path

from main_app.views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
]