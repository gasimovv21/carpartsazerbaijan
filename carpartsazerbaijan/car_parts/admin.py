from django.contrib import admin

from .models import Orders



@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'price_in_town',
        'cargo_price',
        'additional_cost',
        'image',
    )
    search_fields = (
        'id',
        'name',
        'price',
        'price_in_town',
        'cargo_price',
        'additional_cost',
        'image',
    )
    list_filter = (
        'id',
        'name',
        'price',
        'price_in_town',
        'cargo_price',
        'additional_cost',
        'image',
    )
    empty_value_display = '-boş-'