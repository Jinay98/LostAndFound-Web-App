from django.contrib import admin
from accounts.models import UserProfile,ItemData
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ItemData)
