from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_teams, name='get_teams'),
    path('add-team/', views.add_team, name='add_team'),
    path('search-team/', views.search_team, name='search_team'),
    path('stats/<int:team_id>/', views.get_team_stats, name='get_team_stats'),
    path('delete-team/<int:team_id>/', views.delete_team, name='delete_team')
]
