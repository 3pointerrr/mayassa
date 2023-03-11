from django.test import TestCase

from socialmedia.models import SocialMedia
from socialmedia.repository.generator.socialmedia import SocialMediaDataGeneratorLayer



class TestSocialMediaModel(TestCase):


    def setUp(self):
        self.social_media_DGL =  SocialMediaDataGeneratorLayer()
        self.social_media_DGL.create_social_media(total=3)

    def test_str_method(self):
        soc = SocialMedia.objects.first()
        self.assertEqual(str(soc), soc.title)


    def test_verbose_name(self):
        self.assertEqual(SocialMedia._meta.verbose_name,"social media")
        self.assertEqual(
            SocialMedia._meta.verbose_name_plural,
            "social medias"
            )
