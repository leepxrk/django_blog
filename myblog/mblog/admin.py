from django.contrib import admin
from .models import post

# Register your models here.

#admin.site.register(post)

class postAdmin:
    list_display = ('title','tag','pub_date')

admin.site.register(post,postAdmin)