import os 
from django.core.files.uploadedfile import SimpleUploadedFile

from django.test import TestCase
from django.core.exceptions import ValidationError

from banner.models import Banner

class Banner(TestCase):

    def setUp(self):
        self.image = SimpleUploadedFile(
            name="test_image.jpg",
            content=open(os.path.join(os.path.dirname('media/demo/'),'rossFreakOut.png'))
        )


    def test_valid_picture_size(self):
        instance = Banner(
            title = "banner",
            picture = self.image,
            alternate_text = "this is an image"
            
        )
        instance.full_clean()
        self.assertLessEqual(instance.picture.size,1024 * 1024)