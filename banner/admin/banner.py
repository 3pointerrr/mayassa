

from django.contrib import admin
from banner.models.banner import Banner
from django.utils.translation import gettext_lazy as _


@admin.register(Banner)
class Banner(admin.ModelAdmin):
    """ admin for Banner include list display , and list display include 
    title because we want user to just see the title and image, in this list we 
    can see create and modified so we can filter content by created and modified
    we have some options in readonly because the values are auto completing with 
    program , by option add on top user has save option on top of the page and down"""
    list_display = (
        'title',

    )

    search_fields = (
        'title',
    )

    search_help_text = _("Search in services by title")
    
    list_filter = (
        'created',
        'modified'
    )
    readonly_fields = (
        'created',
        'height_field',
        'width_field',
        'modified'
    )
    save_on_top = True