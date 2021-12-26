from .models import Profile, Skill, Message
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Message)
