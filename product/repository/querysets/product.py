from django.db.models import QuerySet


class ProductDataAccessQuerySet(QuerySet):
    

    def get_actives(self,is_active: bool = True):

        return self.filter(is_active=is_active)
    
    def find_by_category(self, category_title):
        return self.filter(category__title=category_title)
    
