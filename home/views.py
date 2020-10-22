from django.shortcuts import render
from meals.models import Meals, Category
from blog.models import Post
from aboutus.models import Why_choose_Us

def home(request):
    meals = Meals.objects.all()[0:6]
    categories = Category.objects.all()
    posts = Post.objects.all()
    latest_post = Post.objects.last()
    choose = Why_choose_Us.objects.all()

    context = {
        "meals": meals,
        'categories':categories,
        "posts":posts,
        "latest_post":latest_post,
        "choose": choose,
    }

    return render(request, "home/index.html", context)


