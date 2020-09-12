from django.urls import path
from .views import meal_list, meal_detail

app_name = "meals"
urlpatterns = [
    path("", meal_list, name = "home"),
    path("meals/<slug:slug>/", meal_detail, name ="detail")
]
