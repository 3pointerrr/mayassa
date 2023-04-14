import os 
from django.core.files.uploadedfile import SimpleUploadedFile

from django.test import TestCase
from django.core.exceptions import ValidationError

from banner.models import Banner

class Banner(TestCase):
    """  The setUp method sets up the test environment by 
    creating a sample image file using SimpleUploadedFile 
    which is later used in the test_valid_picture_size method.
    In the test_valid_picture_size method, a Banner instance is
    created with the sample image, title, and alternate text. The
    full_clean method is called to validate the instance and ensure 
    that the picture field size is not greater than 1MB (1024 * 1024 bytes).
    The assertLessEqual method checks if the picture size is less than or equal
    to 1MB, and raises an assertion error if it is greater than 1MB."""

    def setUp(self):
        """ """
        self.image = SimpleUploadedFile(
            name="test_image.jpg",
            content=open(os.path.join(os.path.dirname('media/demo/'),'rossFreakOut.png'))
        )


    def test_valid_picture_size(self):
        """ """
        instance = Banner(
            title = "banner",
            picture = self.image,
            alternate_text = "this is an image"
            
        )
        instance.full_clean()
        self.assertLessEqual(instance.picture.size,1024 * 1024)