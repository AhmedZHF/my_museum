from django.contrib import admin

# Register your models here.

from .models import  Museum,Topic ,Comment

admin.site.register(Museum)
admin.site.register(Topic)
admin.site.register(Comment)

