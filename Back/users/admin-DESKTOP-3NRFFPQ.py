from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group as DefaultGroup
from django.utils.translation import gettext_lazy as _
from users.models import CustomGroup, CustomUser

admin.site.unregister(DefaultGroup)


@admin.register(CustomGroup)
class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "min_participants", "max_participants", "status")
    filter_horizontal = ("permissions",)
    fieldsets = (
        (
            None,
            {
                "fields": ("name", "status"),
            },
        ),
        (
            "Participant Limits",
            {
                "fields": ("permissions", "min_participants", "max_participants"),
                "classes": (
                    "wide",
                    "extrapretty",
                ),  # Optional: add CSS classes for styling
            },
        ),
    )

    # Optionally, you can add more customization here
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(CustomUser)
class CustomUserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined", "avatar")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "first_name", "last_name", "is_active")
    search_fields = ("email", "mobile", "last_name")

    ordering = ("email",)
