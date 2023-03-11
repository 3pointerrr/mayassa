# valid kardan aksa
from django.core.validators import BaseValidator
from django.core.files.images import get_image_dimensions
#abaad akso migire
from django.core.exceptions import ValidationError
# error default validate kardan django
from django.utils.deconstruct import deconstructible
#serachesh kon


@deconstructible
class DimensionValidator(BaseValidator): # validate kardan abaad aks

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __call__(self, value):
        pic = value.file.open()
        width, height = get_image_dimensions(pic)
        if not (width == self.width and height == self.height):
            raise ValidationError(
                f"Expected dimension is: [{self.width}w, {self.height}h]"
                f" but actual is [{width}w, {height}h]"
            )
