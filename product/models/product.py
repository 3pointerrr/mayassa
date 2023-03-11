from django.db import models
from django.core.validators import FileExtensionValidator

from painless.models.validators import DimensionValidator
from painless.models.mixin_files import PictureOperationMixin,TimeStampMixin


class Product(PictureOperationMixin,TimeStampMixin):

    title = models.CharField(
        max_length=20,
        null=False,
        help_text='product name'
    )

    description = models.TextField(
        unique=False,
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
        validators = [
            DimensionValidator(800, 600),
            #validators abbad
            FileExtensionValidator(   #validator type
                allowed_extensions= [
                    'JPG','JPEG','jpg','jpg','png '
                ]
            )
        ]  
        
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='products',
        help_text='related to product'
    )

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self) -> str:
        return self.title
    
    def __refr__(self) -> str:
        return self.title

