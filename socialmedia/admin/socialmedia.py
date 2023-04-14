from django.contrib import admin

from socialmedia.models.socialmedia import SocialMedia


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):

    
    list_display = (
        'title',
        'created',
        'modified',
    )

    # add search section for title
    search_fields = (
        'title',
    )
    # search hint for search section
    search_help_text = 'search by title'

    # with this option you can filter by created and modified
    list_filter = (
        'created',
        'modified',
    )

    # with this option now we have another save option on top 
    save_on_top=True
