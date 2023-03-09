from django.contrib import admin
from howitwork.models import HowItWork
from django.utils.translation import gettext_lazy as _


@admin.register(HowItWork)
class HowItWorkAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'priority',

    )

    search_fields = (
        'title',
        'priority'
    )

    search_help_text = _("Search in services by title,summary")
    
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