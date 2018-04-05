from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('processing', views.processing, name='processing'),
    path('payment', views.payment, name='payment'),
]
