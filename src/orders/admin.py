from django.contrib import admin
from . import models

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    raw_id_fields = ['book']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(models.Order, OrderAdmin)