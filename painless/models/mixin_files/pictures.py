from django.db import models

class PictureOperationMixin(models.Model):

    height_field = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        editable=False,
        help_text='photos height'
    )

    width_field = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        editable=False,
        help_text='photos width'
    )

    alternate_text = models.CharField(
        max_length=110,
        help_text='describe about photo that is uoloaded.'
                'please write a good description for search engines'
    )

    class Meta:
        abstract =True