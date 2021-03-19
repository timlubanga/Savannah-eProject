from django.contrib import admin
from django.conf import settings
from authentication.models import UserAccount


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email',
                    'auth_provider', 'created_at', "is_active", "is_superuser"]


admin.site.register(UserAccount, UserAdmin)
