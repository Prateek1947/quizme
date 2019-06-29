from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.forms import *
from user.models import User


# Register your models here.
class CustomAdminPanel(UserAdmin):
    add_form = CreateUserForm
    form = UpdateUserForm
    model = User
    fieldsets = (
        (None, {'fields': ('username', 'password', 'following', 'profile_picture')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )


admin.site.register(User, CustomAdminPanel)
