from django.contrib import admin

from .models import *

admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comment)


