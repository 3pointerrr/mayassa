from django.core.management.base import BaseCommand

from socialmedia.repository.generator import social_media_DGL

class Command(BaseCommand):
    """ This is a Django management command that generates social
    media data using a custom module called social_media_DGL. 
    The add_arguments method is used to add custom arguments 
    to the command. In this case, it adds a required argument
    "total" which specifies the number of social media data 
    items to be generated. The handle method is where the actual
    logic of the command is implemented. It retrieves the value 
    of the "total" argument from the options and then creates an
    instance of social_media_DGL. Finally, it calls the create_social_media
    method of the instance to generate social media data.
    """
    def add_arguments(self, parser):
    
        parser.add_argument('total',type=int)


    def handle(self,*args, **options) :
    
        total = options.get('total',5_000)
        DGL = social_media_DGL()
        DGL.create_social_media(total)