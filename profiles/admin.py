from django.contrib import admin
from profiles.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "address", "city", "country",)
    # list_filter = ("created_ad",)
    # readonly_fields = ("created_ad",)
    search_fields = ("address", "city", "country",)

