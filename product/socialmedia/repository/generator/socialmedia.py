from tqdm import tqdm

from django.core.files.uploadedfile import SimpleUploadedFile

from django.conf import settings
from socialmedia.models import SocialMedia
from painless.models.generator import BaseDataGenerator

BASEDIR = settings.BASE_DIR
class SocialMediaDataGeneratorLayer(BaseDataGenerator):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_social_media(self,total):

        objs = [
            SocialMedia(
            title = f"social media -> {self.get_random_person(1)}",
            url = f"url : {self.get_random_person(1)}"
            )
            for i in tqdm(range(total))
        ]

        social_medias = SocialMedia.objects.bulk_create(
            objs,
            batch_size=1_000
        )