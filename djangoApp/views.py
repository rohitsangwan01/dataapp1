from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import StoreInventoryTransactionsForm, StoreCheckoutForm, StoreCheckoutItemsForm
from .models import *
from django.contrib.admin.views.decorators import staff_member_required


# @staff_member_required
# def bust_manufacturer_cache(request, manufacturer_id):
#     pass


def storeInventoryTransactions(request):
	StoreInventory(fk_store_id = form.cleaned_data.get('fk_store_id'), fk_product_id = form.cleaned_data.get('fk_product_id'), mrp = form.cleaned_data.get('mrp'), quantity = form.cleaned_data.get('quantity')).save()
	return HttpResponseRedirect("../")

def showIndex(request):
	form = StoreInventoryTransactionsForm()
	return render(request,'store_inventory_transactions.html',{'form':form})

def saveData(request):
	fk_store = request.POST.get('fk_store')
	fk_product = request.POST.get('fk_product')
	fk_barcode = request.POST.get('fk_barcode')
	mrp = request.POST.get('mrp')
	expiry_date = request.POST.get('expiry_date')
	batch_number = request.POST.get('batch_number')
	txn_type = request.POST.get('txn_type')
	reference_number = request.POST.get('reference_number')
	quantity = request.POST.get('quantity')
	comment = request.POST.get('comment')

	store_obj = Store.objects.get(id=fk_store)
	product_obj = Product.objects.filter(id=fk_product)

	if txn_type == 'stock_transfer':
		qty = product_obj[0].pack_qty - int(quantity)
	elif txn_type == 'stock_return':
		qty = product_obj[0].pack_qty + int(quantity)
	elif txn_type == 'local_purchase':
		qty = product_obj[0].pack_qty - int(quantity)
	elif txn_type == 'stock_audit_adjustment':
		qty = product_obj[0].pack_qty - int(quantity)
	elif txn_type == 'pos_returns':
		qty = product_obj[0].pack_qty + int(quantity)
	
	product_obj.update(pack_qty=qty)

	store_inventory_obj = StoreInventory.objects.filter(fk_store=fk_store,fk_product=fk_product)
	if store_inventory_obj:
		store_inventory_obj.update(mrp=mrp,quantity=qty)
	else:
		StoreInventory(fk_store_id=fk_store,fk_product_id=fk_product,mrp=mrp,quantity=qty).save()	

	# fk_store, fk_product, fk_barcode, mrp, expiry_date, batch_number, txn_type 
	# reference_number, quantity, comment

	StoreCheckout('invoice_number', 'fk_store', 'fk_customer','is_delivery', 'is_online', 'promotions', 'cast_discount', 'sub_total', 'grand_total', 'payments', 'loyalty_point_used', 'wallet_amount_used').save()

	StoreCheckoutItems('fk_store_checkout', 'fk_product', 'qty', 'mrp','sp', 'attributed_cart_discount').save()

	Stocktransfer('order_number', 'sales_invoice_number', 'fk_store').save()


	StocktransferItems('fk_stock_transfer', 'fk_product', 'mrp','expiry_date', 'quantity').save()

	# StoreInventoryTransactions(fk_store_id = fk_store,fk_product_id = fk_product,fk_barcode_id = fk_barcode, mrp = mrp, expiry_date = expiry_date,batch_number = batch_number, txn_type = txn_type,reference_number = reference_number,	quantity = quantity, comment = comment ).save()

	# return HttpResponse("Data Saved. Check in Database")


def checkout(request):
	return render(request,'store_checkout.html',{'form':StoreCheckoutForm(),'form1':StoreCheckoutItemsForm()})

def saveCheckout(request):
	invoice_number = request.POST.get('invoice_number')
	fk_store = request.POST.get('fk_store')
	fk_customer = request.POST.get('fk_customer')
	fk_product = request.POST.get('fk_product')
	is_delivery = request.POST.get('is_delivery')
	if is_delivery:
		is_delivery = True
	else:
		is_delivery = False
	is_online = request.POST.get('is_online')
	if is_online:
		is_online = True
	else:
		is_online = False
	promotions = request.POST.get('promotions')
	if promotions:
		pass
	else:
		promotions = ""
	cast_discount = request.POST.get('cast_discount')
	sub_total = request.POST.get('sub_total')
	grand_total = request.POST.get('grand_total')
	payments = request.POST.get('payments')
	loyalty_point_used = request.POST.get('loyalty_point_used')
	if loyalty_point_used:
		pass
	else:
		loyalty_point_used = ""
	wallet_amount_used = request.POST.get('wallet_amount_used')
	if wallet_amount_used:
		pass
	else:
		wallet_amount_used = ""

	product_obj = Product.objects.get(id=fk_product)
	StoreCheckout(invoice_number=invoice_number,fk_store_id=fk_store,fk_customer_id=fk_customer,is_delivery=is_delivery,is_online=is_online,cast_discount=cast_discount,sub_total=sub_total,grand_total=grand_total,promotions=promotions,wallet_amount_used=wallet_amount_used,loyalty_point_used=loyalty_point_used,payments=payments).save()

	list_of_store_checkouts = [each_store_checkouts for each_store_checkouts in StoreCheckout.objects.all()]

	store_checkout_items_obj = StoreCheckOutItems.objects.filter(fk_product=fk_product)
	if store_checkout_items_obj:
		store_checkout_items_obj.update(qty=product_obj.pack_qty,mrp=grand_total,sp=sub_total,attributed_cart_discount=cast_discount)
	else:
		StoreCheckOutItems(fk_store_checkout_id=list_of_store_checkouts[-1].id,fk_product_id=fk_product,qty=product_obj.pack_qty,mrp=sub_total,sp=payments,attributed_cart_discount=cast_discount).save()

	return HttpResponse("Data Saved. Check in Database")


def store(request):
	microenterpreneur_data = Microenterpreneur.objects.all()
	address_data = Address.objects.all()

	return render(request,'store.html',{'microenterpreneur':microenterpreneur_data,'address':address_data})

def add_store(request):
	name = request.POST.get('name')
	address = request.POST.get('address')
	microenterpreneur = request.POST.get('microenterpreneur')
	store_code = request.POST.get('store_code')


	Store(name=name,fk_address_id=address,fk_microenterpreneur_id=microenterpreneur,store_code=store_code).save()

	microenterpreneur_data = Microenterpreneur.objects.all()
	address_data = Address.objects.all()

	return render(request,'store.html',{'microenterpreneur':microenterpreneur_data,'address':address_data})


def update_address(request):
	address_id = request.GET.get('address_id')
	address_obj = Address.objects.get(id=address_id)
	microenterpreneur_data = Microenterpreneur.objects.all()
	address_data = Address.objects.all()
	city_data = City.objects.all()
	state_data = State.objects.all()

	return render(request,'store.html',{'update_address':address_obj,'city':city_data,'state':state_data,'microenterpreneur':microenterpreneur_data,'address':address_data})

def save_address_update(request):
	address_id = request.POST.get('id')
	name = request.POST.get('name')
	address_line1 = request.POST.get('address_line1')
	address_line2 = request.POST.get('address_line2')
	city = request.POST.get('city')
	state = request.POST.get('state')
	pincode = request.POST.get('pincode')
	geolocation = request.POST.get('geolocation')

	city_id = City.objects.get(name=city).id
	state_id = State.objects.get(name=state).id

	address_obj = Address.objects.filter(id=address_id)
	address_obj.update(name=name,address_line1=address_line1,address_line2=address_line2,city_id=city_id,state_id=state_id,pincode=pincode,geolocation=geolocation)
	microenterpreneur_data = Microenterpreneur.objects.all()
	address_data = Address.objects.all()

	return render(request,'store.html',{'microenterpreneur':microenterpreneur_data,'address':address_data})

def delete_address(request):
	address_id = request.GET.get('address_id')
	Address.objects.get(id=address_id).delete()
	microenterpreneur_data = Microenterpreneur.objects.all()
	address_data = Address.objects.all()

	return render(request,'store.html',{'microenterpreneur':microenterpreneur_data,'address':address_data})

def microenterpreneur(request):
	address_data = Address.objects.all()

	return render(request,'microenterpreneur.html',{'address':address_data})



def update_microenterpreneur_address(request):
	address_id = request.GET.get('address_id')
	address_obj = Address.objects.get(id=address_id)
	address_data = Address.objects.all()
	city_data = City.objects.all()
	state_data = State.objects.all()

	return render(request,'microenterpreneur.html',{'update_address':address_obj,'city':city_data,'state':state_data,'address':address_data})

def delete_microenterpreneur_address(request):
	address_id = request.GET.get('address_id')
	Address.objects.get(id=address_id).delete()
	address_data = Address.objects.all()

	return render(request,'microenterpreneur.html',{'address':address_data})


def save_microenterpreneur_address_update(request):
	address_id = request.POST.get('id')
	name = request.POST.get('name')
	address_line1 = request.POST.get('address_line1')
	address_line2 = request.POST.get('address_line2')
	city = request.POST.get('city')
	state = request.POST.get('state')
	pincode = request.POST.get('pincode')
	geolocation = request.POST.get('geolocation')

	city_id = City.objects.get(name=city).id
	state_id = State.objects.get(name=state).id

	address_obj = Address.objects.filter(id=address_id)
	address_obj.update(name=name,address_line1=address_line1,address_line2=address_line2,city_id=city_id,state_id=state_id,pincode=pincode,geolocation=geolocation)
	address_data = Address.objects.all()

	return render(request,'microenterpreneur.html',{'address':address_data})


def add_microenterpreneur(request):
	name = request.POST.get('name')
	address = request.POST.get('address')
	is_active = request.POST.get('is_active')
	mobile = request.POST.get('mobile')
	email = request.POST.get('email')
	print(is_active,type(is_active))
	if is_active == "True":
		is_active = 1
	else:
		is_active = 0

	Microenterpreneur(name=name,fk_address_id=address,is_active=is_active,mobile=mobile,email=email).save()

	address_data = Address.objects.all()

	return render(request,'microenterpreneur.html',{'address':address_data})


def customer(request):
	address_data = Address.objects.all()
	return render(request,'customer.html',{'address':address_data})


def update_customer_address(request):
	address_id = request.GET.get('address_id')
	address_obj = Address.objects.get(id=address_id)
	address_data = Address.objects.all()
	city_data = City.objects.all()
	state_data = State.objects.all()

	return render(request,'customer.html',{'update_address':address_obj,'city':city_data,'state':state_data,'address':address_data})

def delete_customer_address(request):
	address_id = request.GET.get('address_id')
	Address.objects.get(id=address_id).delete()
	address_data = Address.objects.all()

	return render(request,'customer.html',{'address':address_data})


def save_customer_address_update(request):
	address_id = request.POST.get('id')
	name = request.POST.get('name')
	address_line1 = request.POST.get('address_line1')
	address_line2 = request.POST.get('address_line2')
	city = request.POST.get('city')
	state = request.POST.get('state')
	pincode = request.POST.get('pincode')
	geolocation = request.POST.get('geolocation')

	city_id = City.objects.get(name=city).id
	state_id = State.objects.get(name=state).id

	address_obj = Address.objects.filter(id=address_id)
	address_obj.update(name=name,address_line1=address_line1,address_line2=address_line2,city_id=city_id,state_id=state_id,pincode=pincode,geolocation=geolocation)
	address_data = Address.objects.all()

	return render(request,'customer.html',{'address':address_data})


def add_customer(request):
	name = request.POST.get('name')
	address = request.POST.get('address')
	mobile = request.POST.get('mobile')
	credit = request.POST.get('credit')
	loyalty_point = request.POST.get('loyalty_point')
	wallet_amount = request.POST.get('wallet_amount')

	Customer(name=name,fk_address_id=address,mobile=mobile,credit=credit,loyalty_point=loyalty_point,wallet_amount=wallet_amount).save()

	address_data = Address.objects.all()

	return render(request,'customer.html',{'address':address_data})


def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(fk_state_id=country_id).all()
    return render(request, 'persons/city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
















