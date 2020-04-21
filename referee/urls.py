from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_referees, name='get_referees'),
    path('add-referee/', views.add_referee, name='add_referee'),
    path('search-referee/', views.search_referee, name='search_referee'),
    path('delete-referee/<int:referee_id>/', views.delete_referee, name='delete_referee')
]