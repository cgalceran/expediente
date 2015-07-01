import django_tables2 as tables
from models import Expediente

class ExpedienteTable(tables.Table):
    class Meta:
        model = Expediente
        #fields = ('distribuidora','name','rendicion','total','nota')
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}