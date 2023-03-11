from tqdm import tqdm

import secrets

from product.models import Product


class SocialMediaDataGeneratorLayer:
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_social_media(self,total):
        objs = [
            Product(
            title = f"product {secrets.token_urlsafe(10)}",
            description = f"url{secrets.token_urlsafe(10)}"
            )
            for i in tqdm(range(total))
        ]

        social_medias = Product.objects.bulk_create(
            objs,
            batch_size=1_000
        )