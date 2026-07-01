
from django.contrib import admin
from django.urls import path
from blog.views import *
from services.views import *
from contacts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog_home),
    path('blog_list/', blog_list),
    path('services/', services_home),
    path('services_list/', services_list),
    path('contacts/', contacts_home),
    path('contacts_list/', contacts_list),
]



