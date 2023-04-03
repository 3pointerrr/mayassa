from django.db import models

from painless.mixin_files.mixins import TimeStampMixin

class Tag(TimeStampMixin):

    title = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        help_text='tag name'
    )

    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return self.title