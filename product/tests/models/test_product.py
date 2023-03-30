from django.test import TestCase

from product.models import product
from product.repository.generator.product import ProductDataGeneratorLayer



class TestSocialMediaModel(TestCase):


    def setUp(self):
        self.product_DGL =  ProductDataGeneratorLayer()
        self.product_DGL.create_category(total=3)

    def test_str_method(self):
        pro = product.objects.first()
        self.assertEqual(str(pro), pro.title)


    def test_verbose_name(self):
        self.assertEqual(product._meta.verbose_name,"product")
        self.assertEqual(
            product._meta.verbose_name_plural,
            "social medias"
            )
