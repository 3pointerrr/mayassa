from django.db.models import Manager

from ..querysets.product import ProductDataAccessQuerySet

class ProductDataAccessLayerManager(Manager):    

    def get_queryset(self):
        return ProductDataAccessQuerySet(self.model,using=self._db)
    
    def find_by_category(self, category_title):
        return self.get_queryset().find_by_category(category_title)