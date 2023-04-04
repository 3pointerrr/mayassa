from tqdm import tqdm
import functools
from django.core.files.uploadedfile import SimpleUploadedFile
import os 
from django.conf import settings
from product.models import (
    Product,
    Category,
    Tag
)
from painless.models.generator import BaseDataGenerator
BASE_DIR = settings.BASE_DIR

class ProductDataGeneratorLayer(BaseDataGenerator):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_product_categories(self,total):
        objs = [
            Category(
                title=f"category {self.get_random_secret(15)}",
            )
            for i in tqdm(range(total))
        ]
        categories = Category.objects.bulk_create(
            objs,
            batch_size=10_000
        )
    def create_tags(self,total):
        objs = [
            Tag(
                title=f"Tag {self.get_random_secret(15)}",
            )
            for i in tqdm(range(total))
        ]
        tags = Tag.objects.bulk_create(
            objs,
            batch_size=10_000
        )    
        
    def create_product(self,categories,total):

        demo_pic_path = os.path.normpath(f"media\demo\gradient.jpg")
        with open (os.path.join(BASE_DIR,demo_pic_path),mode="rb") as pic_file :
            pic = pic_file.read()
            objs = [
                Product(
                title = f"product {self.get_random_words(5)}",
                description = f"url {self.get_random_secret(7)}",
                size = 10,
                category  = self.get_random_obj(categories),
                picture = SimpleUploadedFile(
                    name=self.get_random_pic_name(format='jpg'),
                    content=pic
                    ),
                    alternate_text = self.get_random_secret(6)
                )
                for i in tqdm(range(total))
            ]
    
            products = Product.objects.bulk_create(
                objs,
                batch_size=10_000
            )
            return products
        
    def join_tags_to_posts(self,products,tags,item_per_object):
        joiner = functools.partial(
            self.add_to_m2m,
            tags,
            'tags',
            item_per_object
        )
        result = list(tqdm(map(joiner,products)))
