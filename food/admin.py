from django.contrib import admin
from .models import Menu
from .models import UserProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Menu)