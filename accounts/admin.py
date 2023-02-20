# Import Admin classes
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Import Model
from .models import User, VerifyEmail
from django.contrib.auth.models import Group

# Import Forms
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("__str__", 'is_admin', 'join_date')
    list_filter = ("is_admin",)
    search_fields = ("email",)
    ordering = ("id",)
    filter_horizontal = ()

    fieldsets = (
        (None, {"fields": ('email', 'password')}),
        ("Personal Information", {"fields": ("first_name", "last_name", "birthday")}),
        ("permissions", {"fields": ('is_admin', 'is_active')})
    )
    add_fieldsets = (
        ("Create User", {
            "fields": ("email", "password1", "password2", "first_name", "last_name", "birthday", "is_admin",)
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)


class VerifyEmailAdmin(admin.ModelAdmin):
    class Meta:
        model = VerifyEmail

    list_display = ("email", "is_verified", "created")
    list_filter = ("is_verified",)


admin.site.register(VerifyEmail, VerifyEmailAdmin)
