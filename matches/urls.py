from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_matches, name='get_matches'),
    path('add-match/', views.add_match, name='add_match'),
    path('search-match/', views.search_match, name='search_match'),
    path('stats/<int:match_id>/', views.get_match_stats, name='get_match_stats'),
    path('delete-match/<int:match_id>/', views.delete_match, name='delete_match')
]
