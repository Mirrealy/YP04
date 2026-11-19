from django.contrib import admin
from .models import Brand, Car


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "created_at")
    search_fields = ("name",)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("author", "name", "year", "price", "status", "popular")
    list_filter = ("author", "status", "genre", "year")
    search_fields = ("model", "ISBN")
    list_editable = ("status",)
