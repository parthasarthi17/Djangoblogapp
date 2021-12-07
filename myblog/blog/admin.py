from django.contrib import admin
from .models import Author, Article, comments, tempUser
# Register your models here.

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(comments)
admin.site.register(tempUser)
