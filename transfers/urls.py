from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_transfers, name='get_transfers'),
    path('add-transfer/', views.add_transfer, name='add_transfer'),
    path('search-transfer/', views.search_transfer, name='search_transfer'),
    path('delete-transfer/<int:transfer_id>/', views.delete_transfer, name='delete_transfer')
]
