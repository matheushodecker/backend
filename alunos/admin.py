from django.contrib import admin
from .models import estado
from .models import cidade

admin.site.register(estado)
admin.site.register(cidade)