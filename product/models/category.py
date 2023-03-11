from django.db import models

from painless.models.mixin_files import TimeStampMixin

class Category(TimeStampMixin):

    title = models.CharField(
        max_length=20,
        unique=True,
        null=False,
        help_text='category name'
    )

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self) -> str:
        return self.title
    
    def __refr__(self) -> str:
        return self.title