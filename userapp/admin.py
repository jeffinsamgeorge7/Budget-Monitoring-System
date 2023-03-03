from userapp.models import Expense
from django.contrib import admin

# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
    list_display =["name","amount","timestamp"]
admin.site.register(Expense,ExpenseAdmin)