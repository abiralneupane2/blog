from django.contrib import admin

from blog.models import Blog, Author, User

# Register your models here.


admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(User)
