from django.db import models

from painless.mixin_files.mixins import PictureOperationMixin,TimeStampMixin


class Product(PictureOperationMixin,TimeStampMixin):

    title = models.CharField(
        max_length=20,
        unique=True,
        null=False,
        help_text='product name'
    )

    description = models.TextField(
        unique=True,
        null=False,
        help_text='explain about product'
    )

    size = models.PositiveIntegerField(
        null=False,
        help_text='size of product'

    )

    picture = models.ImageField(
        max_length=110,
        unique=True,
        null=False,
        height_field='height_field',
        width_field='width_field',
        upload_to='product/',
        help_text='photo of product',
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='products',
        help_text='related to product'
    )


    def __str__(self) -> str:
        return self.title
    
    def __refr__(self) -> str:
        return self.title
