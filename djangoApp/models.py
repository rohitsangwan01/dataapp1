from django.db import models
from .validations import IntegerRangeField
from django.db.models.signals import post_save,pre_save
from django.utils.decorators import method_decorator
from django.dispatch import receiver

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=100)
    address_line1 = models.TextField()
    address_line2 = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    pincode = models.IntegerField(null=True,blank=True)
    geolocation = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f"{ self.name } - { self.address_line1 } - { self.address_line2 }"

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=1)


    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    fk_manufacturer = models.ForeignKey(Manufacturer,
                                        on_delete=models.CASCADE)
    is_active = models.BooleanField(default=1)
    image_link = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    fk_parent_category = models.IntegerField(null=True,blank=True)
    is_active = models.BooleanField(default=1)
    image_link = models.ImageField(upload_to='media/',null=True,blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    article_code = models.CharField(max_length=100,null=True,blank=True)
    fk_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    fk_brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    pack_qty = models.IntegerField(null=True,blank=True)
    metric_unit = models.CharField(max_length=100,null=True,blank=True)
    uom = models.CharField(max_length=100,null=True,blank=True)
    pack_site = models.IntegerField(null=True,blank=True)
    pack_type = models.IntegerField(null=True,blank=True)
    is_active = models.BooleanField(default=1)
    is_online = models.BooleanField(null=True,blank=True)
    is_expirable = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return self.name

class ProductBarCode(models.Model):
    barcode = models.CharField(max_length=150)
    fk_product = models.OneToOneField(Product,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=1)

    def __str__(self):
        return self.barcode

class Customer(Address):
    customer_name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    credit = models.FloatField()
    loyalty_point = models.IntegerField(null=True,blank=True)
    wallet_amount = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.name


class Microenterpreneur(Address):
    microenterpreneur_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=1)
    mobile = models.BigIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Store(Address):
    store_name = models.CharField(max_length=100)
    fk_microenterpreneur = models.ForeignKey(Microenterpreneur,
                                            on_delete=models.CASCADE)
    store_code = models.IntegerField()

    def __str__(self):
        return self.name

class StoreAssortment(models.Model):
    fk_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    fk_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=1)
    min_qty = models.IntegerField(null=True,blank=True)
    max_qty = models.IntegerField(null=True,blank=True)
    sp = models.IntegerField(null=True,blank=True)


class StoreInventoryTransactions(models.Model):

    CHOICES = (
        ('stock_transfer', 'stock_transfer'),
        ('stock_return', 'stock_return'),
        ('local_purchase', 'local_purchase'),
        ('stock_audit_adjustment', 'stock_audit_adjustment'),
        ('pos_returns', 'pos_returns'),
    )

    date = models.DateTimeField(auto_now_add=True)
    fk_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    fk_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    fk_barcode = models.ForeignKey(ProductBarCode, on_delete=models.CASCADE)
    mrp = models.FloatField()
    expiry_date = models.DateField()
    batch_number = models.IntegerField()
    txn_type = models.CharField(max_length=100,choices=CHOICES)
    reference_number = models.IntegerField()
    quantity = models.IntegerField()
    comment = models.CharField(max_length=100)

    class Meta:
        ordering = ['pk']

@receiver(post_save,sender=StoreInventoryTransactions)
def save_profile(sender, instance, **kwargs):
    store_obj = Store.objects.get(id=instance.fk_store.id)
    product_obj = Product.objects.filter(id=instance.fk_product.id)

    print(store_obj,product_obj)

    if instance.txn_type == 'stock_transfer':
        qty = product_obj[0].pack_qty - instance.quantity
    elif instance.txn_type == 'stock_return':
        qty = product_obj[0].pack_qty + instance.quantity
    elif instance.txn_type == 'local_purchase':
        qty = product_obj[0].pack_qty - instance.quantity
    elif instance.txn_type == 'stock_audit_adjustment':
        qty = product_obj[0].pack_qty - instance.quantity
    elif instance.txn_type == 'pos_returns':
        qty = product_obj[0].pack_qty - instance.quantity
    
    product_obj.update(pack_qty=qty)

    store_inventory_obj = StoreInventory.objects.filter(fk_store=instance.fk_store,fk_product=instance.fk_product)
    if store_inventory_obj:
        store_inventory_obj.update(mrp=instance.mrp,quantity=qty)
    else:
        StoreInventory(fk_store=instance.fk_store,fk_product=instance.fk_product,mrp=instance.mrp,quantity=qty).save()   




class StoreInventory(models.Model):
    fk_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    fk_product = models.ForeignKey(Product,on_delete=models.CASCADE,default=False)
    mrp = models.FloatField(default=False)
    quantity = models.IntegerField(default=False)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        pass

class StoreCheckout(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    invoice_number = models.CharField(max_length=100)
    fk_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    fk_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    is_delivery = models.BooleanField()
    is_online = models.BooleanField()
    promotions = models.CharField(max_length=100,null=True,blank=True)
    cast_discount = models.FloatField()
    sub_total = models.FloatField()
    grand_total = models.FloatField()
    payments = models.FloatField(null=True,blank=True)
    loyalty_point_used = models.IntegerField(null=True,blank=True)
    wallet_amount_used = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.invoice_number

# @receiver(pre_save,sender=StoreCheckout)
# def save_profile(sender, instance, **kwargs):

#     store_checkout_items_obj = StoreCheckOutItems.objects.filter(fk_store_checkout=instance,fk_product=instance.fk_product)
#     if store_checkout_items_obj:
#         store_checkout_items_obj.update(qty=instance.fk_product.pack_qty,mrp=instance.grand_total,sp=instance.sub_total,attributed_cart_discount=instance.cast_discount)
#     else:
#         StoreCheckOutItems(fk_store_checkout=instance,fk_product=instance.fk_product,qty=instance.fk_product.pack_qty,mrp=instance.grand_total,sp=instance.sub_total,attributed_cart_discount=instance.cast_discount).save()


class StoreCheckOutItems(models.Model):
    fk_store_checkout = models.ForeignKey(StoreCheckout, on_delete=models.CASCADE)
    fk_product = models.ForeignKey(Product, on_delete=models.CASCADE,default=1)
    qty = models.IntegerField()
    mrp = models.FloatField()
    sp = models.CharField(max_length=100)
    attributed_cart_discount = models.FloatField()


class StockTransfer(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    order_number = models.TextField(max_length=50)
    sales_invoice_number = models.TextField(max_length=50)
    fk_store = models.ForeignKey(Store,on_delete=models.CASCADE,default=False)

    def __str__(self):
        return self.order_number


class StocktransferItems(models.Model):
    fk_stock_transfer = models.ForeignKey(StockTransfer,
                                          on_delete=models.CASCADE)
    fk_product = models.ForeignKey(Product,
                                          on_delete=models.CASCADE)
    mrp = models.FloatField()
    expiry_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    fk_address = models.OneToOneField(Address,on_delete=models.CASCADE,null=True,blank=True)
    is_active = models.BooleanField(default=1)
    warehouse_code = models.IntegerField()

    def __str__(self):
        return self.name
