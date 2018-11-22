from django.db import models

# Create your models here.

class CustomerName (models.Model):
	cust_name = models.CharField(max_length = 251, null= True, blank =True)
	status = models.BooleanField(default = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now =True)
	contract_number = models.CharField(max_length = 251, null= True, blank =True)
	cse_name = models.CharField(max_length = 251, null= True, blank =True)
	location = models.CharField(max_length = 501, null= True, blank =True)
	pms = models.CharField(max_length = 251, null= True, blank =True)
	renewed_amount = models.CharField(max_length = 251, null= True, blank =True)
	
	branch_name = models.CharField(max_length = 251, null= True, blank =True)
	expiry_date = models.DateField(null= True, blank =True)
	contract_job = models.CharField(max_length = 251, null= True, blank =True)
	cust_id =models.CharField(max_length = 251, null= True, blank =True)
	cust_tier =models.CharField(max_length = 251, null= True, blank =True)
	contact_number =models.CharField(max_length = 251, null= True, blank =True)
	premise_type = models.CharField(max_length = 251, null= True, blank =True)
	business_segment =models.CharField(max_length = 251, null= True, blank =True)
	renewal_date = models.CharField(max_length = 251, null= True, blank =True)
	basic_value =models.CharField(max_length = 251, null= True, blank =True)
	tax =models.CharField(max_length = 251, null= True, blank =True)

	service =models.CharField(max_length = 251, null= True, blank =True)	
	contract_period_from = models.DateField(null= True, blank =True)
	contract_period_to = models.DateField(null= True, blank =True)
