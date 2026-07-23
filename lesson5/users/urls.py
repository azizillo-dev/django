from django.urls import path
from .views import home, users_list 


urlpatterns = [
    path('', home),
    path('users-list/', users_list),
]
