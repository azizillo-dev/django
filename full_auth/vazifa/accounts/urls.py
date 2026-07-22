from django.urls import path
from .views import RegisterView, dashboard, LoginView, logout_view, ProfileView, ProfileUpdateView, ChangePassView



app_name = 'accounts'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-update/', ProfileUpdateView.as_view(), name='update'),
    path('change-pass/', ChangePassView.as_view(), name='change_pass'),
]








