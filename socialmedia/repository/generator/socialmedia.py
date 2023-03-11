from tqdm import tqdm

import secrets

from socialmedia.models import SocialMedia


class SocialMediaDataGeneratorLayer:
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_social_media(self,total):
        objs = [
            SocialMedia(
            title = f"social media{secrets.token_urlsafe(10)}",
            url = f"url{secrets.token_urlsafe(10)}"
            )
            for i in tqdm(range(total))
        ]

        social_medias = SocialMedia.objects.bulk_create(
            objs,
            batch_size=1_000
        )