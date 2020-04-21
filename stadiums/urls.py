from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_stadiums, name='get_stadiums'),
    path('add-stadium/', views.add_stadium, name='add_stadium'),
    path('search-stadium/', views.search_stadium, name='search_stadium'),
    path('delete-stadium/<int:stadium_id>/', views.delete_stadium, name='delete_stadium')
]
