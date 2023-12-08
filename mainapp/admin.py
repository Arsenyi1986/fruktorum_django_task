from django.contrib import admin

from .models import Link
from .models import ParsedData, Collection

admin.site.register(Link)
admin.site.register(ParsedData)
admin.site.register(Collection)