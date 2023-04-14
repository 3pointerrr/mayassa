from django.db import models
from django.utils.translation import gettext_lazy as _
from painless.mixin_files.mixins import TimeStampMixin,PictureOperationMixin
from painless.models.validators import DimensionValidator
from django.core.validators import FileExtensionValidator
from painless.models import pict
class Banner(TimeStampMixin,PictureOperationMixin):
    """ these are banner models of the mayassa website including title and picture """
    title = models.CharField(
        _("Title"),
        max_length=20,
        unique=True,
        null=False,
        help_text=_("title of banner")
    )

    picture = models.ImageField(
        _("picture"),
        max_length=110,
        height_field='height_field',
        width_field='width_field',
        upload_to='banner/',
        validators=[
        DimensionValidator(1920,1080),
        FileExtensionValidator("png","PNG","jpg")
        ]
    )

    alternate_text = models.CharField(
        max_length=110,
        help_text=_("alternate for banner for situation like when image"
                    " is not loaded correctly")
    )
    
    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title