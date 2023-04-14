from django.db import models
from django.utils.translation import gettext_lazy as _
from painless.mixin_files.mixins import TimeStampMixin

class SubmitOrder(TimeStampMixin):
    """ """
    title = models.CharField(
        _("Title"),
        max_length=20,
        unique=True,
        null=False,
        help_text=_("how it work title")
    )

    picture = models.ImageField(
        _("picture"),
        max_length=110,
        height_field='height_field',
        width_field='width_field',
        upload_to='submitorder/'
    )

    height_field = models.PositiveSmallIntegerField(
        _("height_field"),
        null = True,
        blank = True,
        editable=False,
        help_text=_("size of the picture height ")
    )
    
    width_field = models.PositiveSmallIntegerField(
        _("width_field"),
        null = True,
        blank = True,
        editable=False,
        help_text=_("size of the picture height ")
    )

    alternate_text = models.CharField(
        max_length=110,
        help_text=_("alter text for submit order picture")
    )
    
    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title