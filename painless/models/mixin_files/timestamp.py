from django.db import models

class TimeStampMixin(models.Model):
    
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=('automatic insertation of record')
    )

    modified = models.DateTimeField(
        auto_now=True,
        help_text= 'automatic modification of record'
    )

    class Meta:
        abstract =True