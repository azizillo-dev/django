from django.urls import path
from .views import LandingPageView, DashboarView, RegisterView, LoginView, LogoutView, ProfileUpdateView, ProfileView


app_name = 'accounts'



urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('dashboard/', DashboarView.as_view(), name='dashboard'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update/', ProfileUpdateView.as_view(), name='update'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

































