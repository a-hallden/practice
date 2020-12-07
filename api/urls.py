from django.urls import path

from . import views

urlpatterns = [
    path('', views.OMDBView.as_view(), name='omdb_view'),
    path('favorites/', views.FavoriteListView.as_view(), name='favorite_list'),
    path('favorites/<int:id>/', views.FavoriteDetailView.as_view(), name='favorite_detail'),
]
