from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django import forms


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm
    list_display = ("email","role","id")
    ordering = ("email",)
    list_filter = ('role',)

    fieldsets = (
        ("Personal details", {'fields': ('email', 'password', 'first_name', 'last_name', 'mobile','image', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser')}),
        ('Address details', {'fields': ('pincode', 'city','state', 'country','address')}),
        ('Organization', {'fields': ('organization',)}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 
            'password', 
            'role')
            }
            ),
        )

    filter_horizontal = ()

admin.site.register(User, CustomUserAdmin)