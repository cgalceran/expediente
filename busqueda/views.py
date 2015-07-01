from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

from models  import Expediente, Item 


class ListadoExpedientes(ListView):
	"""docstring for ListadoExpedientes"""
	
	model  = Expediente
	template_name = 'busqueda/item_list.html'
	