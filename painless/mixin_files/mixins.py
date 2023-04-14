from django.db import models

class TimeStampMixin(models.Model):
    """ we brought created and modified here so we wont 
    write them in every model"""
    
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=('automatic insertion of record')
    )

    modified = models.DateTimeField(
        auto_now=True,
        help_text= 'automatic modification of record'
    )

    class Meta:
        """ the model is marked as abstract and Django will not create a
        database table for this model. Instead, it will be used as a base
        class for other models to inherit from."""
        abstract =True
        

class PictureOperationMixin(models.Model):
    """ """

    height_field = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        editable=False,
        help_text='photos height'
    )

    width_field = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        editable=False,
        help_text='photos width'
    )

    alternate_text = models.CharField(
        max_length=110,
        help_text='describe about photo that is uploaded.'
                'please write a good description for search engines'
    )

    class Meta:
        """ the model is marked as abstract and Django will not create a
        database table for this model. Instead, it will be used as a base
        class for other models to inherit from."""
        abstract =True