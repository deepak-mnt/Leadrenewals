from django.shortcuts import render, HttpResponse
from login.models import CustomerName
from django.http import JsonResponse
import json

from .models import *

# Create your views here.
def home(request):

	# contract_number = list(set([cust.contract_number for cust in CustomerName.objects.all()]))
	customer_ins = CustomerName.objects.all()
	cse_name = list(set([cust.cse_name for cust in customer_ins]))
	pms_data = list(set([cust.pms for cust in customer_ins]))
	print("pms data",pms_data)
	print("cse name print",cse_name[0:10])

	# cust_name =  list(set([cust.cust_name for cust in CustomerName.objects.all()]))
	
	# args = {'contract_number' :contract_number, 'cust_name': cust_name}
	args = {'cse_name': cse_name, 'pms_data': pms_data}

	# return render(request, 'renewal form.html', args)
	return render(request, 'test.html', args)

def onchange_contractnumber(request):

	contractnumber = request.GET.get('contractnumber', None)
	cse_name = request.GET.get('csename', None)
	expiry_date_object =  CustomerName.objects.filter(contract_number=str(contractnumber), cse_name=str(cse_name)).first()
	expiry_date =  expiry_date_object.expiry_date
	customerdetail =  CustomerName.objects.filter(contract_number=str(contractnumber), cse_name=str(cse_name))
	print("count",len(customerdetail))
	# customer_name =  list(set([customer.cust_name for customer in customerdetail]))
	# cse_data =  list(set([customer.cse_name for customer in customerdetail]))
	# location_data =  list(set([customer.location for customer in customerdetail]))
	pms_data =  list(set([customer.pms for customer in customerdetail]))
	basic_value = list(set([customer.basic_value for customer in customerdetail]))
	print("=========basic value=========",basic_value)
	
	# cust_name_html = "<option> Select Customer</option>"
	# cse_name_html = "<option> Select cse name</option>"
	# location_html = "<option>Select location</option>"

	# for custname in customer_name:
	# 	cust_name_html += '<option>' + custname + '</option>'
	# for cse in cse_data:
	# 	cse_name_html += '<option>' + cse + '</option>'
	# for location in location_data	:
	# 	location_html += '<option>' + location + '</option>'
	if len(basic_value) > 1:
		basic_value_html = "<option>Select basic</option>"
	else:
		basic_value_html = ""
	if len(pms_data) > 1:	
		pms_html = "<option>Select pms</option>"
	else:	
		pms_html = ""
	for pms in pms_data:
		pms_html += '<option>' + pms + '</option>'
	for basic in basic_value:
		basic_value_html += '<option>' + basic + '</option>'	
	# pms_html += '<option><select><option>Others</option>'
	
	pms_master_list = ['BBS', 'GSS', 'IFM', 'SPS', 'BSS', 'IPM', 'IMM', 'TSPR', 'PRT', 'PPS', 'PAT', 'PET', 'ILM', 'BPS', 'ISM', 'PSS', 'TSPO', 'GPM', 'FUM', 'TMG']
	pms_master_list = list(set(pms_master_list)-set(pms_data))
	pms_master_list_html = ""
	for pms in pms_master_list:
		pms_master_list_html += '<option>' + pms + '</option>'
	# pms_html += '</select></option>'
	table_data = """<tr style="background:#8becd6" >
   	  <th class="text-center">Customer Name</th>
      <th class="text-center">Location</th>
      <th class="text-center">PMS</th>
      <th class="text-center">Basic Value</th>
                           </tr>"""
	
	for cust in customerdetail:
		table_data += "<tr><td>"+cust.cust_name+"</td><td>"+cust.location+"</td><td>"+cust.pms+"</td><td>"+cust.basic_value+"</td></tr>"
	# data = { 'expiry_date': expiry_date, 'cust_name': cust_name_html, 'cse_name': cse_name_html, 'location':location_html, 'pms': pms_html  }
	data = {'expiry_date': expiry_date,'table_data': table_data, 'pms_list':pms_html, 'basic_value':basic_value_html,'pms_master_list':pms_master_list_html}
	return JsonResponse(data)

def onchange_cse_name(request):
	print("in onchange_cse_name method")
	cse_name = request.GET.get('csename', None)
	print("cse_name",cse_name)
	# expiry_date_object =  CustomerName.objects.filter(contract_number=contractnumber).first()
	# expiry_date =  expiry_dat<tr style="background:#8becd6" >
	customerdetail =  CustomerName.objects.filter(cse_name=cse_name)
	contract_numbers =  list(set([customer.contract_number for customer in customerdetail]))
	# cse_data =  list(set([customer.cse_name for customer in customerdetail]))
	# location_data =  list(set([customer.location for customer in customerdetail]))
	# pms_data =  list(set([customer.pms for customer in customerdetail]))
	if len(contract_numbers) > 1:
		contract_number_html = "<option> Select Contract Number</option>"
	else:
		contract_number_html = ""	
	# cust_name_html = "<option> Select Customer</option>"
	# cse_name_html = "<option> Select cse name</option>"
	# location_html = "<option>Select location</option>"
	# pms_html = "<option>Select pms</option>"
	for contract_no in contract_numbers:
		contract_number_html += '<option>' + contract_no + '</option>'

	# for custname in customer_name:
	# 	cust_name_html += '<option>' + custname + '</option>'
	# for cse in cse_data:
	# 	cse_name_html += '<option>' + cse + '</option>'
	# for location in location_data	:
	# 	location_html += '<option>' + location + '</option>'
	# for pms in pms_data:
	# 	pms_html += '<option>' + pms + '</option>'
	data = { 'contract_number': contract_number_html }
	# data = { 'expiry_date': expiry_date, 'cust_name': cust_name_html, 'cse_name': cse_name_html, 'location':location_html, 'pms': pms_html  }

	return JsonResponse(data)

def delete_row(request):
	row_no = request.GET.get("row_no")
	table_data = request.GET.get("table_values_test")
	print("table_data======",table_data)
	table_data = table_data.replace("[","").replace("]","")
	table_data = table_data.replace("},{","}|{")
	table_data = table_data.split("|")
	new_table = [json.loads(x) for x in table_data if json.loads(x).get("row_no") != row_no]
	print("new_table",new_table)
	# print("table_list",table_list)
	# print("typeof table_data",type(table_data))	
	# table_data_json = json.load(table_data)
	# print("json table data",table_data_json)


def submit_customer_details(request):
	
	if request.method == 'POST' :

		table_data = request.POST.get('hidden_field')
	
		# expirydate = request.POST.get('expirydate')
		# print("expirydate",expirydate)
		print("table len",len(table_data))


		print("in submit method table_data",table_data)

		contractnumber = request.POST.get('contractnumber')
		# cust_name = request.POST.getlist('cust')
		cse_name = request.POST.get('csename')

		customerdetail =  CustomerName.objects.filter(contract_number=str(contractnumber), cse_name=str(cse_name)).first()
		
		pms_id = request.POST.get('pms_id')
		basic_value = request.POST.get('basic_value')
		service = request.POST.get('service')
		renewed_amount = request.POST.get('renewed_amount')
		contract_period_from = request.POST.get('contract_period_from')
		contract_period_to = request.POST.get('contract_period_to')

		if len(table_data) > 2:
			print("in if table_data")
			table_data = table_data.replace("[","").replace("]","")
			table_data = table_data.replace("},{","}|{")
			table_data = table_data.split("|")
			table_data = [json.loads(x) for x in table_data]
			print("in loop",table_data)
		else:
			table_data = []
			print("else of table_data")	
		# print("table type",type(table_data))	
		if service != "" and renewed_amount != "":
			table_data.append({
				"pms_id":pms_id,
				"basic_value":basic_value,
				"service":service,
				"renewed_amount":renewed_amount,
				"contract_period_from":contract_period_from,
				"contract_period_to":contract_period_to
				})	
			
		if table_data:
			for table in table_data :
				print("======table=======",table)
				customer_ins = ""
				customer_ins = CustomerName.objects.filter(
					contract_number=str(contractnumber), 
					# cust_name=str(cust_name[0]),
					cse_name = str(cse_name),
					# location = str(location),
					pms = str(table.get("pms_id")),
					basic_value = str(table.get("basic_value"))
					).first()
				print("customer_ins",customer_ins)
				customer_ins.service = str(table.get("service"))
				customer_ins.renewed_amount = str(table.get("renewed_amount"))
				customer_ins.contract_period_from = str(table.get("contract_period_from"))
				customer_ins.contract_period_to = str(table.get("contract_period_to"))
				customer_ins.save()
		# location = request.POST.get('location')
		# pms = request.POST.get("pms")
		# renewed_amount = request.POST.get('renewedamount')

		input_table_data = request.POST.get('input_hidden_field')

		pms_master_id = request.POST.get('pms_master_id')
		input_basic_value = request.POST.get('input_basic_value')
		input_service = request.POST.get('input_service')
		# renewed_amount = request.POST.get('renewed_amount')
		input_contract_period_from = request.POST.get('input_contract_period_from')
		input_contract_period_to = request.POST.get('input_contract_period_to')

		if len(input_table_data) > 2:
			print("in if table_data")
			input_table_data = input_table_data.replace("[","").replace("]","")
			input_table_data = input_table_data.replace("},{","}|{")
			input_table_data = input_table_data.split("|")
			input_table_data = [json.loads(x) for x in input_table_data]
		else:
			input_table_data = []	

		if input_basic_value != "" and input_service != "":
			input_table_data.append({
				"pms_master_id":pms_master_id,
				"input_basic_value":input_basic_value,
				"input_service":input_service,
				"input_contract_period_from":input_contract_period_from,
				"input_contract_period_to":input_contract_period_to
			})	
		print("input_table_data",input_table_data)
		if input_table_data:
			for table in input_table_data:
				print("========input table========",table)
				print("===========date=======",table.get("input_contract_period_to"))
				# customer_ins = ""
				customer_ins = CustomerName(
					cust_name = str(customerdetail.cust_name),
					contract_number = str(contractnumber), 
					cse_name = str(cse_name),
					location = str(customerdetail.location),
					pms = str(table.get("pms_master_id")),
					branch_name = str(customerdetail.branch_name),
					expiry_date = table.get("input_contract_period_to"),
					contract_job = str(customerdetail.contract_job),
					cust_id = str(customerdetail.cust_id),
					cust_tier = str(customerdetail.cust_tier),
					contact_number = str(customerdetail.contact_number),
					premise_type = str(customerdetail.premise_type),
					business_segment = str(customerdetail.business_segment),
					basic_value = str(table.get("input_basic_value")),
					service = str(table.get("input_service")),
					contract_period_from = str(table.get("input_contract_period_from")),
					contract_period_to = str(table.get("input_contract_period_to"))
				)
				customer_ins.save()

		return render (request, 'thank_you.html', {'msg':'successfuly updated'})
	else:
		print("else")	
		# return render (request, 'error.html', {'msg':'data not found'})