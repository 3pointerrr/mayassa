from django.test import TestCase

from product.models import Category
from product.repository.generator import BDG

class TestBlogCategoryModel(TestCase):

    def setUp(self):
        self.blog_dgl = BDG()
        self.blog_dgl.create_product_category(10)
    
        # self.cat = Category.objects.create(title='ali')

    def test_str_method(self):
        cat = Category.objects.first()
        self.assertEqual(str(cat), cat.title)

    def test_verbose_name(self):
        self.assertEqual(Category._meta.verbose_name, 'Category')
        self.assertEqual(Category._meta.verbose_name_plural, 'Categories')


    