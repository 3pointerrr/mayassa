from django.contrib import admin

from product.models import Category, Product


#eijad attach dar model  #zamani ke yek be chand darim   
class ProductInlineAdmin(admin.StackedInline):
    model = Product
    min_num = 1 #min tedad atachment  #in ba extra jam mishe neshun mide!
    max_num = 6  #max tedad atachment
    extra = 1  #chandta chandta add-extra biare
    verbose_name = 'atachhhhhhment'  #esme guruhe attach
    can_delete = True  #tik delete baghale attach miad
    show_change_link = True
    

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

#ezafe kardan attach be model
    inlines = (
        ProductInlineAdmin,
    )