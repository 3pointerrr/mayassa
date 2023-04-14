from django.core.validators import BaseValidator
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible


@deconstructible
class DimensionValidator(BaseValidator):
    """
        It is used to validate the dimensions of
        an uploaded image file. The validator checks 
        if the width and height of the image are less
        than or equal to the specified dimensions in 
        the constructor. If the dimensions of the image
        exceed the specified dimensions, a ValidationError 
        is raised with a custom error message.
    """
    code = "dimension value"

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __call__(self, value):
        pic = value.file.open()
        width, height = get_image_dimensions(pic)
        if(width > self.width or height > self.height):
            raise ValidationError(
                _(
                    
                f"Expected dimension is:[{self.width}w , {self.height}h]"
                f"but actual is [{width}w {height}h]"
                    
                ),
                code=self.code
            )