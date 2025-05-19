from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin    

from accounts.models import User, Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("id", "email", "phone_number", "first_name", "last_name", "is_active", "is_staff")
    list_display_links = ("id", "email", "phone_number", "first_name", "last_name")
    search_fields = ("email", "phone_number", "first_name", "last_name")
    list_filter = ("is_active", "is_staff")
    ordering = ['email']  

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "phone_number", "avatar")}),
        (("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    list_display_links = ("id", "user")
    search_fields = ("user",)

    inlines = [CartItemInline]