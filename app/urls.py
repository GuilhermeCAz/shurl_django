from django.urls import path

from app.views import docs, index, redirect_to_original

urlpatterns = [
    path('', index, name='index'),
    path('docs/', docs, name='docs'),
    path('<str:slug>/', redirect_to_original, name='redirect_to_original'),
]
