from django.contrib import admin
from .models import EnglishPhrases

class EnglishAdmin(admin.ModelAdmin):
	search_fields = ['english']
	list_display = ['english']
	ordering  = ['english']
	list_filter  = ['uzbek']

admin.site.register(EnglishPhrases, EnglishAdmin)
