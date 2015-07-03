#modulos que sirven para hacer el management command
from django.core.management.base import BaseCommand
from busqueda.models import Expediente, Item

#Modulos que sirven para importar los datos 
from busqueda.latin_to_ascii import latin1_to_ascii
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time



#Get the Page making a POST request with the Requests Module
#---------------------------------------------------------------------------------------------------
def busqueda_tabla(expediente):
	if len(expediente)==10:
		expediente = '00'+expediente
	elif len(expediente)==11:
		expediente = '0'+expediente	

	payload = {'cudap': 'EXP-S01:'+'%s' % expediente,
			   'seach': 'Buscar',
			   'isNew':'true'}
	req = requests.post("http://expedientes.mecon.gov.ar/finddoc2/finddoc/VerExpediente", data=payload)
	soup = BeautifulSoup(req.content)#Contenido entero de la pagina
	tfoot = soup.findAll('tfoot')#Contenido de las tablas
	trs = tfoot[0].findAll('tr')# Dentro de la tabla que me interesa la [0], busco los <tr> y dejo fuera la linea de encabezado
	flag = False
	headers = []
	response = []
	for tr in trs:
		if not flag:
			for td in tr.contents:
				if td != '\n':
					headers.append(td.text)
			flag = True
			continue
		else:
			tds = tr.findAll('td')
			data = {}
			for  i, td in enumerate(tds):
				data[latin1_to_ascii(headers[i])] = td.text
				response.append(data)
	return data
	time.sleep(2)

#Define the Management Command with BaseCommand
#---------------------------------------------------------------------------------------------------

class Command(BaseCommand):

	def parse_date(self, date):
		date = date.upper().replace('DIC','DEC').replace('ENE','JAN').replace('ABR','APR').replace('AGO','AUG')
		return datetime.strptime(date, '%d-%b-%Y - %H:%M:%S')

	def handle(self, *args, **options):
		SinTransferir = '-'
		auxiliar = 0

		for each in Expediente.objects.all():
			try:
				busqueda = busqueda_tabla(each.name)
				auxiliar = auxiliar + 1
				if auxiliar > 10:
					time.sleep(15)
					auxiliar = 0
				fecha_destino = self.parse_date(busqueda['Fecha de envio'])
				fecha_recepcion = self.parse_date(busqueda['Fecha de recepcion'])
				if busqueda['Fecha de recepcion'] == SinTransferir:
					continue
				item, created = Item.objects.get_or_create(expediente=each, fecha_recepcion=fecha_recepcion, fecha_envio=fecha_destino,
														   destino=busqueda['Destino'], origen=busqueda['Origenes'])
				if created:
					print 'Se crearon datos en la base sobre el expediente: %s' % each.name
				else:
				    print 'El expediente %s no tuvo movimiento' % each.name
			
			except IndexError:
				continue   





