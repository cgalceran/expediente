from django import template
from busqueda.models import Item
from datetime import date

register = template.Library()


@register.filter
def calculate_days_at_location(value):	
	if value != None:
		total = date.today() - value.date()
		total = total.days
	else:
		total = 0		
	return total

	 

@register.filter
def if_not_empty(value):
	if value is None:
		pass
	else:
		return value

@register.filter
def days_since_creation(value):
	if value != None:
		total = date.today() - value
		total = total.days
	else:
		total = 0		
	return total