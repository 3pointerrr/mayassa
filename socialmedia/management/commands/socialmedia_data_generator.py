from django.core.management.base import BaseCommand

from socialmedia.repository.generator import social_media_DGL

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('total',type=int)


    def handle(self,*args, **options) :
        total = options.get('total',5_000)
        DGL = social_media_DGL()
        DGL.create_social_media(total)