from django.contrib import admin

from currency.models import Currency


class ListDisplayAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'charcode',
        'date',
        'rate'
    )


admin.site.register(Currency, ListDisplayAdmin)
