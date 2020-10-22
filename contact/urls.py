from django.urls import path
from .views import send_email, send_success

app_name = "contact"
urlpatterns = [
    path("", send_email, name = "send_email"),
    path("success/", send_success, name = "send_success"),
]
