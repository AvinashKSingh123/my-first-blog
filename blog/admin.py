from django.contrib import admin

#Added Manually
from .models import Post

# Register your models here.

admin.site.register(Post)