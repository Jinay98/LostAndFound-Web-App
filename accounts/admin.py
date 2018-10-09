from django.contrib import admin
from .models import ItemData,RequestData, ClaimData
# Register your models here.

admin.site.register(ItemData)
admin.site.register(RequestData)
admin.site.register(ClaimData)