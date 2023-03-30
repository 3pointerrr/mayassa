from django.core.management.base import BaseCommand

from product.repository.generator import product_DGL

from product.models import Category
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--cat-total',type=int,default=10)
        parser.add_argument('--prod-total', type=int, default=100)


    def handle(self,*args, **options) :
        cat_total = options.get('cat_total',5_00)
        prod_total = options.get('prod_total', 100)
        DGL = product_DGL()
        categories = DGL.create_product_categories(cat_total)
        categories = list(Category.objects.all())
        products = DGL.create_product(categories, prod_total)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(products)} products.'))