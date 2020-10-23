from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("meal", include("meals.urls", namespace="meals")),
    path("reservation/", include("reservation.urls", namespace="reservation")),
    path("blog/", include("blog.urls", namespace="blog")),
    path("about-us/", include("aboutus.urls", namespace="aboutus")),
    path("contact/", include("contact.urls", namespace="contact")),
    path("", include("home.urls", namespace="home")),

    path('summernote/', include('django_summernote.urls')),
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#if you wanna customize your admin panel here is the way 
admin.site.site_header = "Danishyar Restaurant Admin"
admin.site.site_title = "رستورانت دانشیار"
admin.site.site_index_title = "welcome to Danishyar Restaurant admin panel"
