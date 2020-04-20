from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_matches, name='get_matches'),
]