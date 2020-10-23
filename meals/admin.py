from django.contrib import admin
from .models import Meals, Category
from django_summernote.admin import SummernoteModelAdmin


class MealsModelAdmin(SummernoteModelAdmin, admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['category','people','price','created']
    search_fields = ['name','description']
    list_filter = ('people','category')

admin.site.register(Meals, MealsModelAdmin)
admin.site.register(Category)
