from django.contrib import admin

from .models import ExcelModel


class ExcelAdmin(admin.ModelAdmin):
    fields= ['file']


admin.site.register(ExcelModel,ExcelAdmin)
