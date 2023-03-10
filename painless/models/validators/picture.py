from django.core.validators import BaseValidator
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible


@deconstructible
class DimensionValidator(BaseValidator):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __call__(self, value):
        with value.file.open() as pic:
            width, height = get_image_dimensions(pic)
            if(width > self.width or height > self.height):
                raise ValidationError(
                    _(
                    
                    f"Expected dimension is:[{self.width}w , {self.height}h]"
                    f"but actual is [{width}w {height}h]"
                    
                    )
                )