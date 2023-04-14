from django.contrib import admin
from howitwork.models import HowItWork
from django.utils.translation import gettext_lazy as _


@admin.register(HowItWork)
class HowItWorkAdmin(admin.ModelAdmin):
    """ admin for HowItWork include list display , and list display include 
    title and priority because we want user to just see the them, in this list filter we 
    can see create and modified so we can filter content by created and modified and
    we can search by title and priority we have some options in readonly because 
    the values are auto completing with program , by option add on top user has 
    save option on top of the page and down"""
    list_display = (
        'title',
        'priority',

    )

    search_fields = (
        'title',
        'priority'
    )

    search_help_text = _("Search in services by title,priority")
    
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