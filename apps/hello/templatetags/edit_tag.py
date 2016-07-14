
from django.core.urlresolvers import reverse
from django.template import Library

register = Library()


@register.simple_tag
def edit_link(obj):
    if obj:
        url = "admin:%s_%s_change" % (
            obj._meta.app_label,
            obj._meta.module_name,
        )
        result = reverse(url, args=(obj.pk, ))
    else:
        result = reverse("admin:index")
    return result
