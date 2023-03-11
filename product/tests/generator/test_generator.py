
from django.test import TestCase
from socialmedia.models.socialmedia import SocialMedia
from socialmedia.repository.generator.socialmedia import SocialMediaDataGeneratorLayer

class DataGeneratorTest(TestCase):

    def setUp(self):
        self.DGL = SocialMediaDataGeneratorLayer()
        self.total_social_media = 30

        self.socialmedias = self.DGL.create_social_media(self.total_social_media)

    def test_create_social_media(self):

        actual = SocialMedia.objects.count()
        excepted = 30 

        self.assertEqual(
            actual,
            excepted,
            msg=f"Constant Total SocialMedia Expected `{excepted}`"
            f"but actual is `{actual}`"
        )