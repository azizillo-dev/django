from django.urls import path
from .views import RegisterView, dashboard



urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('register/', RegisterView.as_view(), name='register'),
]








