from django.shortcuts import render, get_object_or_404
from . models import Post, Category


def post_list(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, "blog/post_list.html", context)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    
    context = {
        'post': post
    }
    return render(request, "blog/post_detail.html", context)