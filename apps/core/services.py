from django.db.models import QuerySet

#  internals


class CoreService(object):

    @classmethod
    def search(cls, qs: QuerySet, query: str, *args, **kwargs) -> QuerySet:
        pass
