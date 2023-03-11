from django.db.models import QuerySet


class SocialMediaQuertySet(QuerySet):
    

    def get_actives(self,is_active: bool = True):

        return self.filter(is_active=is_active)