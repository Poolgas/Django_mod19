from django.contrib import admin
from .models import Buyer, Game


# Register your models here.

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    search_fields = ('name', 'age')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'description', 'age_limited')
    list_filter = ('title', 'cost', 'age_limited')
    search_fields = ('title', 'cost', 'age_limited')
    list_per_page = 5


