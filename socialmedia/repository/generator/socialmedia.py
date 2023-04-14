from tqdm import tqdm

from django.core.files.uploadedfile import SimpleUploadedFile

from django.conf import settings
from socialmedia.models import SocialMedia
from painless.models.generator import BaseDataGenerator

BASEDIR = settings.BASE_DIR
class SocialMediaDataGeneratorLayer(BaseDataGenerator):
    """
    This code defines a class called SocialMediaDataGeneratorLayer which inherits from a
    BaseDataGenerator class. It has a constructor that calls the constructor of the base
    class using super() method. The main method of this class is create_social_media(total)
    which takes a parameter total indicating the number of objects to be created.
    In this method, a list comprehension is used to create a list of SocialMedia objects. 
    The title and url fields of each object are set to a randomly generated string using 
    the get_random_person() method from the base class. The tqdm() method is used to display
    a progress bar while creating the objects.Finally, the bulk_create() method of the SocialMedia
    model is called with the list of objects and a batch_size of 100 to efficiently create the 
    objects in the database.
    """
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
            batch_size=1_00
        )