from django import template
from busqueda.models import Item
from datetime import date

register = template.Library()


@register.filter
def calculate_days_at_location(value):	
	total = date.today() - value.date()
	return total.days 

@register.filter
def if_not_empty(value):
	if value is None:
		pass
	else:
		return value

