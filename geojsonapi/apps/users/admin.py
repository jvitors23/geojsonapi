from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ("id",)
    list_display = ("email", "name")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),)
