from django.contrib import admin

from django.contrib.auth.models import User
User.objects.filter(is_superuser=True)
