from django.contrib import admin

from product.models.tag import Tag
from product.models.product import Product


class ProductInlineAdmin(admin.StackedInline):
    
    model = Product
    extra = 1
    show_change_link = True

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    

    list_display = (
        'title',
        'created',
        'modified',
    )

    search_fields = (
        'title',
    )
    #inlines = (ProductInlineAdmin,)
    search_help_text = 'search by title'

    list_filter = (
        'created',
        'modified',
    )

    save_on_top=True