from django.contrib import admin

from account.models import Profile, RegisteredBookModel

admin.site.register(Profile)
admin.site.register(RegisteredBookModel)