from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Short, Photo, Category, Size, Color, Comment, Order, OrderItem
# vita

admin.site.register(User, UserAdmin)
admin.site.register(Short)
admin.site.register(Photo)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Comment)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'email', 'phone'
                    'address', 'country', 'subject', 'comment',
                    'created', 'updated']
    list_filter = ['created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order)
admin.site.register(OrderItem)