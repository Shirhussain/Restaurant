from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


class PostModelAdmin(SummernoteModelAdmin, admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['author','category','tags','created']
    search_fields = ['title','content']
    list_filter = ('category','tags',)

admin.site.register(Post, PostModelAdmin)
admin.site.register(Category)
admin.site.register(Comment)
