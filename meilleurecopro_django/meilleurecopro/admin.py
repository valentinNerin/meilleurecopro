from django.contrib import admin
from .models import Estate

# Register your models here.
class EstateAdmin(admin.ModelAdmin):
  list_display = ("city", "zip_code", "dept_code", "condominium_expenses", "ad_url")   
  
admin.site.register(Estate, EstateAdmin)