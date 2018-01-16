from django import template
from core.models import AppCustomization

register = template.Library()

@register.simple_tag()
def show_customizations_title():
    try:
        q = AppCustomization.objects.get(id=1)
        return q.product_title
    except AppCustomization.DoesNotExist:
        return False

@register.simple_tag()
def show_customizations_color():
    try:
        q = AppCustomization.objects.get(id=1)
        return q.color_hex
    except AppCustomization.DoesNotExist:
        return '2185d0'

@register.simple_tag()
def show_customizations_logo():
    try:
        q = AppCustomization.objects.get(id=1)
        return q.logo_image.url
    except AppCustomization.DoesNotExist:
        return None

@register.simple_tag()
def show_customizations_bg_image():
    try:
        q = AppCustomization.objects.get(id=1)
        image = q.app_background_photo.url
        option = q.app_background_options
        if option == 'T':
            return 'url(' +image+ '); background-repeat: repeat;'
        else:        
            return 'url(' +image+ '); background-repeat: no-repeat; background-size: cover;'
    except AppCustomization.DoesNotExist:
        return ' none;'

@register.simple_tag()
def show_customizations_favicon():
    try:
        q = AppCustomization.objects.get(id=1)
        return q.app_favicon.url
    except AppCustomization.DoesNotExist:
        return ''                