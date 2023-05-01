import secrets
import os

from django.core.files.uploadedfile import SimpleUploadedFile
from tqdm import tqdm
from django.conf import settings

from product.models import Category,Product
from painless.models.generator import BaseDataGenerator


BASE_DIR = settings.BASE_DIR


class BlogDataGeneratorLayer(BaseDataGenerator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def create_product_category(self, total):       #total>> yani ta chanta data gharare besaze
        objs= [
            Category(title=f'Category{self.get_random_secret(5)}')  #baraye sakht fake obj va estefade mojadad az commands
            for i in tqdm(range(total))
        ]
                #comprihension khat payin
                
        categories = Category.objects.bulk_create(objs,batch_size=10_000)
                    #bulk_create besurate dasteyi mire misaze

        return categories
    


    #     for i in tqdm(range (total)):        #tqdm >> sakht saritar obj ha
    #         Category.objects.create(title=f"category{i}")
    



    def create_posts(self, total, category):
        demo_pic_path = os.path.normpath(f'media/demo/demo.jpg')
        with open(os.path.join(BASE_DIR, demo_pic_path), mode='rb') as pic_file:
            pic = pic_file.read()
            objs= [
                Product(
                    title=f'title-{self.get_random_secret(3)}',
                    description = self.get_random_sentences(5),
                    size = self.get_random_numeric(),
                    category = self.get_random_obj(category),
                    picture = SimpleUploadedFile(name=f'generated-pic-{self.get_random_secret(3)}', content=pic),
                    alternate_text = self.get_random_word(4)[:3],
                )
                for i in tqdm(range(total))
            ]
            posts = Product.objects.bulk_create(objs, batch_size=10_000)
            return posts