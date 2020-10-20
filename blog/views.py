from django.shortcuts import render, get_object_or_404
from . models import Post, Category
from taggit.models import Tag


def post_list(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, "blog/post_list.html", context)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'post': post,
        'categories':categories,
        'tags':tags,
    }
    return render(request, "blog/post_detail.html", context)


def post_by_tag(request, tag):
    post_tags = Post.objects.filter(tags__name__in=[tag])

    context = {
        'posts':post_tags
    }
    return render(request, "blog/post_list.html", context)


def post_by_category(request, category):
    post_categories = Post.objects.filter(category__name = category)

    context = {
        'posts':post_categories
    }
    return render(request, "blog/post_list.html", context)

