from django.contrib import admin
from .models import Creator, Developer, Framework, Language

admin.site.register(Creator)
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Developer)
