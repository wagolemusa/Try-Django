from django.contrib import admin
# Register your models here.

from .models import Post

# this is the in built function which register post model into admin sites.
admin.site.register(Post) 

