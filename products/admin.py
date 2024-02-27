from django.contrib import admin
from products.models import Product, SKU


@admin.register(SKU)
class SKUAdmin(admin.ModelAdmin):
    list_display = ("product", "size", "selling_price")
    ordering = ("-id",)
    search_fields = ("product__name",) # To search SKUs based on product name
    fields = (
        ("product","size"),
        ("cost_price", "platform_commission"),
    )
    autocomplete_fields = ("product",)
    readonly_fields = ("id",)

class SKUInline(admin.StackedInline):
    # For display in products admin
    model = SKU
    extra = 0
    ordering = ("-id",)
    readonly_fields = ("size", "selling_price")
    fields = (
        (readonly_fields),
        ("cost_price", "platform_commission")
    )
    show_change_link = True



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "managed_by", "ingredients")
    ordering = ("-id",)
    search_fields = ("name",)
    list_filter = ("is_refrigerated", "category")
    fields = (
        ("name"),
        ("category", "is_refrigerated"),
        "description",
        ("id", "created_at", "edited_at"),
        ("ingredients", "managed_by"),
    )
    autocomplete_fields = ("category", "managed_by")
    readonly_fields = ("id", "created_at", "edited_at")
    inlines=(SKUInline,)


class ProductInline(admin.StackedInline):
    # For display in CategoryAdmin
    model = Product
    extra = 0
    ordering = ("-id",)
    readonly_fields = ("name", "is_refrigerated")
    fields = (readonly_fields,)
    show_change_link = True

