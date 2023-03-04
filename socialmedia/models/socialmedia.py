from django.db import models

from painless.mixin_files.mixins import TimeStampMixin

class SocialMedia(TimeStampMixin):

    title = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        help_text='this is socialmedia like instagram'
    )

    url = models.URLField(
        max_length=250,
        help_text='url of socialmedia'
    )
