from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class Product(models.Model):
    """
    Very basic structure. To be further built up.
    """

    name = models.CharField(
        _("display name"),
        max_length=150,
        unique=True,
        help_text=_("This will be displayed to user as-is"),
    )
    description = models.TextField(
        _("descriptive write-up"),
        unique=True,
        help_text=_("Few sentences that showcase the appeal of the product"),
    )
    ingredients = models.CharField(
        _("ingredients detail"),
        max_length=500,
        blank=True, # To avoid the default values and flexibility in adding products
        null=True,
        help_text=_("Few sentences that provide the ingredients detail"),
    )
    is_refrigerated = models.BooleanField(
        help_text=_("Whether the product needs to be refrigerated"),
        default=False,
    )
    category = models.ForeignKey(
        "categories.Category",
        related_name="products",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    managed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="managed_products",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.name = self.name.strip().title()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        # Just to be explicit.
        db_table = "product"
        ordering = []
        verbose_name = "Product"
        verbose_name_plural = "Products"




class SKU(models.Model):

    product = models.ForeignKey(
        "products.Product",
        related_name="sku",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    size = models.PositiveSmallIntegerField(
        _("Size for the product(grams)"),
        blank=True,
    )
    selling_price = models.PositiveSmallIntegerField(
        _("selling price (Rs.)"),
        default=0,
        help_text=_("Price payable by customer (Rs.)"),
    )
    cost_price = models.PositiveSmallIntegerField(
        _("Cost price (Rs.)"),
        default=0,
        help_text=_("Cost Price of the product (Rs.)"),
    )
    platform_commission = models.PositiveSmallIntegerField(
        _("Platform price (Rs.)"),
        default=0,
        help_text=_("Price incurred on the platform (Rs.)"),
    )

    def validate_unique(self, exclude=None):
        if self.size is not None and self.product is not None:
            queryset = SKU.objects.filter(product=self.product, size=self.size)
            if self.pk:
                queryset = queryset.exclude(pk=self.pk)
            if queryset.exists():
                raise ValidationError(
                    {'size': _('Size must be unique for each product.')},
                    code='unique_together',
                )

    def save(self, *args, **kwargs):
        self.full_clean()
        self.selling_price=self.cost_price+self.platform_commission
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} (Rs. {self.selling_price}/{self.size} grams)"

    class Meta:
        db_table = "sku"
        ordering = []
        verbose_name = "Store Keeping Unit"
        verbose_name_plural = "Store Keeping Units"