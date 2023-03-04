from django.contrib import admin

from product.models.category import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'created',
        'modified',
    )

    search_fields = (
        'title',
    )

    search_help_text = 'search by title'

    list_filter = (
        'created',
        'modified',
    )

    save_on_top=True