from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from taggit.models import Tag

from . models import Post, Category, Comment
from . forms import CommentForm


def post_list(request):
    posts = Post.objects.all()

    #search
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)|
            Q(tags__name__icontains=search_query)
        ).distinct()
        
    

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts': posts
    }
    return render(request, "blog/post_list.html", context)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    comments = Comment.objects.filter(post=post)
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post 
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'categories':categories,
        'tags':tags,
        'comments':comments,
        'comment_form':comment_form,
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

