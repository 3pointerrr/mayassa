from django.db import models

from painless.mixin_files.mixins import PictureOperationMixin,TimeStampMixin

from django.utils.translation import gettext_lazy as _
class Product(PictureOperationMixin,TimeStampMixin):

    title = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        help_text='product name'
    )

    description = models.TextField(
        unique=True,
        null=False,
        max_length=255,
        help_text='explain about product'
    )

    size = models.PositiveIntegerField(
        null=False,
        help_text='size of product'

    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='products',
        help_text='related to product'
    )

    picture = models.ImageField(
        max_length=110,
        height_field='height_field',
        width_field='width_field',
        upload_to='product/',
        help_text='photo of product',
    )


    
    alternate_text = models.CharField(
        max_length=110,
        help_text=_("banner")
    )


    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return self.title
