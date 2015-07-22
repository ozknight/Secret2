from django.contrib import admin
from .models import Company, CompanyStatus
# Register your models here.


class CompanyApprovalAdmin(admin.StackedInline):
    model = CompanyStatus
    can_delete = False
    verbose_name_plural = 'Approval Status'


class CompanyAdminView(admin.ModelAdmin):
    fieldsets = [
        ('Created', {'fields': ['owner']}),
        ('Company Information', {'fields': [
            'logo',
            'name',
            'address',
            'country',
            'province',
            'postal_code',
            'email',
            'website',
        ]}
        ),
    ]
    inlines = [CompanyApprovalAdmin]


admin.site.register(Company, CompanyAdminView)
