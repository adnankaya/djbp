from django.core.paginator import (Paginator,
                                   EmptyPage,
                                   PageNotAnInteger)


def paginate_objects(objects, page, per_page=10):
    """Returns paginated list of given objects
    Parameters:::
    objects: QuerySet
    page: int
    per_page: int
    ::: returns paginated object list
    """
    paginator = Paginator(objects, per_page=per_page)
    try:
        paginated_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        paginated_list = paginator.page(number=1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        paginated_list = paginator.page(number=paginator.num_pages)

    return paginated_list
