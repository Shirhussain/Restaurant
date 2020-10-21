from django.urls import path
from .views import aboutus_list

app_name = "aboutus"
urlpatterns = [
    path("", aboutus_list, name = "aboutus"),
]
