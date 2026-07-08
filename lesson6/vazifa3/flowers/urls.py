from django.urls import path
from .views import *


urlpatterns = [
    path("", home_page, name="home_page"),
    path("create/", create_flower, name="create"),
    path("detail/<int:id>/", detail, name="detail"),
    path("delete/<int:id>/", delete, name="delete")
]


