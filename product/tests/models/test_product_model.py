from django.test import TestCase

from product.models import Product
from product.repository.generator import BDG

class TestBlogProductModel(TestCase):

    def setUp(self):
        self.blog_dgl = BDG()
        self.cats = self.blog_dgl.create_product_category(10)
        self.blog_dgl.create_posts(30, self.cats)
    
        # self.cat = Category.objects.create(title='ali')

    def test_str_method(self):
        pro = Product.objects.first()
        self.assertEqual(str(pro), pro.title)

    def test_verbose_name(self):
        self.assertEqual(Product._meta.verbose_name, 'Product')
        self.assertEqual(Product._meta.verbose_name_plural, 'Products')