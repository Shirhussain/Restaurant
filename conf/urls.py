from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("meals.urls", namespace="meals")),
    path("reservation/", include("reservation.urls", namespace="reservation")),
    path("blog/", include("blog.urls", namespace="blog")),
    path("about-us/", include("aboutus.urls", namespace="aboutus")),
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

