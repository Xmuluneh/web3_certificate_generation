from django.contrib import admin
from connection.models import Account, Assets

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Assets)
class AssetAdmin(admin.ModelAdmin):
    pass
