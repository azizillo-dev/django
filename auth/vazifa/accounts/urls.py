from django.urls import path
from .views import RegisterView, home, LoginView




urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', home, name = 'home'),
    path('login/', LoginView.as_view(), name='login')
]


