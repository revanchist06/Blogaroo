from django.contrib import admin
from .models import BPost
# Register your models here.

@admin.register(BPost)
class AdminPost(admin.ModelAdmin):
    list_display = ["title", "slug", "user" , "publish"]
    list_filter = ["user", "publish"]
    prepopulated_fields = {"slug":("title",)}