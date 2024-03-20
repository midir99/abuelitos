from django import template
from django.core import cache
from django.db import models as db_models

from .. import choices, models

register = template.Library()


@register.inclusion_tag("civilizations/components/pagination.html")
def show_pagination(paginator, page_obj, query_dict=None, page_kwarg="page"):
    ctx = {
        "page_obj": page_obj,
        "page_range": paginator.get_elided_page_range(page_obj.number),
        # "pagination_required": paginator.count > 100,
        "pagination_required": True,
        "paginator": paginator,
    }
    if query_dict is not None:
        qd = query_dict
        if page_kwarg in query_dict:
            qd = query_dict.copy()
            qd.pop(page_kwarg)

        query_string = qd.urlencode()
        ctx["query_string"] = f"&{query_string}" if query_string else ""
    return ctx
