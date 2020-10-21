from django.shortcuts import render
from .models import AboutUs, Restaurant_History, Why_choose_Us, Chef


def aboutus_list(request):
    about_us = AboutUs.objects.last()
    history = Restaurant_History.objects.last()
    choose = Why_choose_Us.objects.all()
    chefs = Chef.objects.all()

    context = {
        'about_us':about_us,
        'history':history,
        'choose':choose,
        'chefs':chefs
    }
    return render(request, "aboutus/about.html", context)



