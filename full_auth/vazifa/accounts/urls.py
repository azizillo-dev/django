from django.urls import path
from .views import RegisterView, dashboard, LoginView



urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]








