from administrator.models import Budget, Department, Head
from django.contrib import admin

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display =["name","balance","timestamp","budgetsum",'expsum']
    readonly_fields =["balance"]

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Budget)
admin.site.register(Head)


