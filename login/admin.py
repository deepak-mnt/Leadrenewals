from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import CustomerName

class CustomerNameResource(resources.ModelResource):
	class Meta:
		model = CustomerName
		fields = ('id','cust_name','contract_number', 'branch_name','expiry_date','contract_job','cust_id','cust_tier','cse_name','contact_number','location','premise_type','business_segment','pms','renewal_date','basic_value','tax','renewed_amount')


class CustomerNameAdmin(ImportExportModelAdmin):
	list_display = ('id','cust_name','contract_number', 'branch_name','expiry_date','contract_job','cust_id','cust_tier','cse_name','contact_number','location','premise_type','business_segment','pms','renewal_date','basic_value','tax','renewed_amount')
	list_display_links = ('id',)
	resource_class = CustomerNameResource

admin.site.register(CustomerName,CustomerNameAdmin)