from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Slider

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')


from django.contrib import admin
from .models import Texture, Color, Size, UsageArea, Product


@admin.register(Texture)
class TextureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hex_code')
    search_fields = ('name',)
    readonly_fields = ('hex_code',)  # if you want it non-editable, otherwise remove this line


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'width', 'height')
    search_fields = ('width', 'height')


@admin.register(UsageArea)
class UsageAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'texture', 'color', 'size', 'created_at')
    list_filter = ('texture', 'color', 'size', 'usage_areas')
    search_fields = ('name', 'description')
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ('usage_areas',)
    readonly_fields = ('created_at', 'updated_at')
