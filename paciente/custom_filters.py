from django import template

register = template.Library()

@register.filter(name='format_date')
def format_date(value):
    return value.strftime('%B')  # Retorna o nome completo do mês
