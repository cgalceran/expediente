from django.contrib import admin
from .models import Tema, PermisoExpediente, Provincia, Distribuidora, Item, Expediente

# Register your models here.

class PermisoAdmin(admin.ModelAdmin):
	filter_horizontal = ['temas',]


class ItemInLine(admin.TabularInline):
	model = Item
	extra = 0
	readonly_fields = ['origen', 'destino', 'fecha_envio', 'fecha_recepcion']

class ExpedienteAdmin(admin.ModelAdmin):
	inlines = [ItemInLine,]


admin.site.register(Expediente, ExpedienteAdmin)
admin.site.register(Item)
admin.site.register(PermisoExpediente, PermisoAdmin)
admin.site.register(Tema)
admin.site.register(Provincia)
admin.site.register(Distribuidora)