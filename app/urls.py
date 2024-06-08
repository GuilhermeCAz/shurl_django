from django.urls import path

from app.views import index, redirect_to_original

urlpatterns = [
    path('', index, name='index'),
    path('<str:slug>/', redirect_to_original, name='redirect_to_original'),
]
