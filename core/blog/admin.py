from django.contrib import admin
from .models import Category,Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # فیلدهایی که می‌خواهید برای پروفایل در ادمین نمایش داده شود
    list_display = ('title','author', 'status') 
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # فیلدهایی که می‌خواهید برای پروفایل در ادمین نمایش داده شود
    list_display = ('name',) 