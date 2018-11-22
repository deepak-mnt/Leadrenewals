from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'^$', views.home),
	url(r'^$', views.home, name = 'home'),
	url(r'^ajax/onchange_contractnumber/$', views.onchange_contractnumber, name='onchange_contractnumber'),
	url(r'^ajax/onchange_cse_name/$', views.onchange_cse_name, name='onchange_cse_name'),
	url(r'^ajax/delete_row/$', views.delete_row, name='delete_row'),
	# url(r'^ajax/onchange_cust/$', views.onchange_cust, name='onchange_cust'),
	url(r'^submit_customer_details/$', views.submit_customer_details, name = 'submit_customer_details'),
	# url(r'^$', views.home, name = 'home'),
]

