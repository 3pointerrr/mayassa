from django.contrib import admin

from product.models.product import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

#namayesh sutunha
    list_display = (
        'title',
        'created',
        'modified',
    )
    autocomplete_fields = (
        'category',
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


#baraye security centere payin
    readonly_fields = (
        'created',
        'modified',
        'height_field',
        'width_field'
    )
#ghabeliat guruh bandi kardan
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
        (('picture zone'), {
            'classes': (
                'collapse',
            ),              #show-hide guruh
            'fields': (
                'picture',
                'height_field',
                'width_field',
            )
        })
)