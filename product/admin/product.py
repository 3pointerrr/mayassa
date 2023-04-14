from django.contrib import admin

from product.models.product import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

# display columns
    list_display = (
        'title',
        'created',
        'modified',
    )
    autocomplete_fields = (
        'category',
                )
# search 
    search_fields = (
        'title',
    )
#search hint
    search_help_text = 'search by title'

#add filter section
    list_filter = (
        'created',
        'modified',
    )

#add save on top of the page
    save_on_top=True


# make fields read only due to security 
    readonly_fields = (
        'created',
        'modified',
        'height_field',
        'width_field'
    )
# grouping option 
    fieldsets = (
        (('product information'), {
            'fields': (
                'title',
                'description',
                'size',
                
            )
        }),
        (('category choose'), {
            'classes': (
                'collapse',
            ),
            'fields': (
                'category',
                'alternate_text'
            )
        }),
        
        (('tag choose'), {
            'classes': (
                'collapse',
            ),
            'fields': (
                'tags',
            )
        }),
        
        (('picture zone'), {
            'classes': (
                'collapse',
            ),              #show-hide group
            'fields': (
                'picture',
                'height_field',
                'width_field',
            )
        })
)