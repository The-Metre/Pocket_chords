from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, Artist, Track, Chords, Watchlist

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', ]

# register all existing models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Artist)
admin.site.register(Track)
admin.site.register(Chords)
admin.site.register(Watchlist)