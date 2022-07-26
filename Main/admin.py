from django.contrib import admin
from Main.models import Flight,Flight_Book,Airlines

admin.site.register(Flight)
admin.site.register(Airlines)
admin.site.register(Flight_Book)