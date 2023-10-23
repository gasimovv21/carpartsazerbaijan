from django.contrib import admin

from .models import Orders


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'part',
        'brand',
        'price',
        'price_in_town',
        'cargo_price',
        'additional_cost',
        'image',
        'color',
    )
    search_fields = (
        'id',
        'name',
        'part',
        'brand',
        'price',
        'price_in_town',
        'cargo_price',
        'additional_cost',
        'image',
        'color',
    )
    list_filter = (
        'id',
        'name',
        'part',
        'brand',
        'price',
        'price_in_town',
        'cargo_price',
        'additional_cost',
        'image',
        'color',
    )
    empty_value_display = '-boş-'