from django.contrib import admin
from .models import estado
from .models import cidade
from .models import pessoa

admin.site.register(estado)
admin.site.register(cidade)
admin.site.register(pessoa)