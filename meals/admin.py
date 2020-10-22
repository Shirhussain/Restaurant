from django.contrib import admin
from .models import Meals, Category
from django_summernote.admin import SummernoteModelAdmin


class MealsModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Meals, MealsModelAdmin)
admin.site.register(Category)
