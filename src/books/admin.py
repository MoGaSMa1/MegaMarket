from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
# Register your models here.



admin.site.register(models.Author)
admin.site.register(models.Series)
admin.site.register(models.Publish)
admin.site.register(models.Gener)
admin.site.register(models.Book)
