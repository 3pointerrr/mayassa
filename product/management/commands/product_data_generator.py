from django.core.management.base import BaseCommand



from product.repository.generator import BDG

#in dastoorat runevisi az doc commands be hamin esmha!
# python manage.py (esm-file) (total)

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--cat-total', type=int, default=5)  #sakht total

    def handle(self, *args, **kwargs):     
        total = kwargs.get('total',10_000)
        CC = BDG()        #sakht obj az generator
        created_category = CC.create_product_category(total)   #tolid obj
        posts = CC.create_posts(2_000, created_category)
