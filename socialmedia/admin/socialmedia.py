from django.contrib import admin

from socialmedia.models.socialmedia import SocialMedia


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):

    #namayesh sutunha
    list_display = (
        'title',
        'created',
        'modified',
    )

#search 
    search_fields = (
        'title',
    )
#zire search hint mizare
    search_help_text = 'search by title'

#sakht jadval filterha
    list_filter = (
        'created',
        'modified',
    )

#save va dokmehaye payin balaham bashe
    save_on_top=True
