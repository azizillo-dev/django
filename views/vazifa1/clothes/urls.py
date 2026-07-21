from django.urls import path
from .views import home, ClothesListView, CreateClothes

urlpatterns = [
    path('', home, name='home'),
    path('clothes-list/',ClothesListView.as_view(), name='list'),
    path('create/', CreateClothes.as_view(), name='create')
]




