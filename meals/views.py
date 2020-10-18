from django.shortcuts import get_object_or_404, render
from . models import  Meals, Category

def meal_list(request):
    meals = Meals.objects.all()
    categories = Category.objects.all()
    context = {
        'meals':meals,
        'categories': categories
        }
    return render(request, "meals/list.html", context)


def meal_detail(request, slug):
    detail = get_object_or_404(Meals,slug=slug)

    context = {
        "meal_detail":detail,
    }
    return render(request, "meals/detail.html", context)


