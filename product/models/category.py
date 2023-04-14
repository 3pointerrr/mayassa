from django.db import models

from painless.mixin_files.mixins import TimeStampMixin

class Category(TimeStampMixin):
    """ """

    title = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        help_text='category name'
    )

    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return self.title