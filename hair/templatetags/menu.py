from django import template

from hair.models import Page

register = template.Library()


@register.inclusion_tag("hair/menu_tpl.html", takes_context=True)
def show_menu(context):
    path = context["request"].path
    pages = Page.objects.all()
    return {"path": path, "pages": pages}
