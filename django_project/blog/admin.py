from django.contrib import admin
from .models import Post

# add things to change admin page
admin.site.register(Post)