from django.core.management.base import BaseCommand
from products.models import SKU

class Command(BaseCommand):
    help = 'Update price fields in SKUs'

    def handle(self, *args, **options):
        # Update price fields in SKUs
        skus = SKU.objects.all()
        for sku in skus:
            selling_price = sku.selling_price
            # Rounding off to avoid changes in selling price since both cost price and commission will round off and decrease the selling price
            platform_commission = round(selling_price * 0.25)
            cost_price = selling_price - platform_commission
            sku.platform_commission = platform_commission
            sku.cost_price = cost_price
            sku.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully updated price fields in SKUs'))
