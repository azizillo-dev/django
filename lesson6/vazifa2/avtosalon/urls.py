from django.urls import path
from .views import *

urlpatterns = [
    path("", home_page, name="home_page"),
    path("create/", create_car, name="create_car"),
    path("delete/<int:pk>/", delete_car, name="delete_car"),
    path("detail/<int:pk>/", detail_car, name="detail_car")
]


