from django.contrib import admin
from .models import CountNumber, Profie


# Register your models here.
class CountNumberAdmin(admin.ModelAdmin):
    list_display = ('numbers',)


admin.site.register(CountNumber, CountNumberAdmin)
admin.site.register(Profie)
