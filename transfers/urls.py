from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_transfers, name='get_transfers'),
]