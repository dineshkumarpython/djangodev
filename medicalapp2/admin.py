from django.contrib import admin
from .models import Num, Appointment, DepartmentList, DocterList, Sample
# Register your models here.
admin.site.register(Num)
admin.site.register(Appointment)
admin.site.register(DepartmentList)
admin.site.register(DocterList)
admin.site.register(Sample)
