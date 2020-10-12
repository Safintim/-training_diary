from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from django.contrib.auth import get_user_model


admin.site.unregister(Group)

User = get_user_model()


@admin.register(User)
class UserAdminCustom(UserAdmin):
    list_display = list_display_links = (
        'id',
        'email',
    )

    fieldsets = (
        ('Личная информация', {
            'fields': ('email', 'password'),
        }),
        ('Тип пользователя', {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        ('Даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    ordering = ('id', )

    search_fields = ('email',)
