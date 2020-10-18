from django.urls import path
from .views import reserve_table

app_name = "reservation"
urlpatterns = [
    path("", reserve_table, name = "reserve_table"),
]
