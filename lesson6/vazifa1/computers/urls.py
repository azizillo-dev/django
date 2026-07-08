from django.urls import path
from .views import *


urlpatterns = [
    path("create/", create_computer, name="create_computer"),
    path("", home_page, name="home_page"),
    path("delete/<int:pk>/", delete_computer, name="delete_computer"),
]



