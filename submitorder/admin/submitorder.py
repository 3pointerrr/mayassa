

from django.contrib import admin
from submitorder.models.submitorder import SubmitOrder
from django.utils.translation import gettext_lazy as _


@admin.register(SubmitOrder)
class HowItWorkAdmin(admin.ModelAdmin):
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