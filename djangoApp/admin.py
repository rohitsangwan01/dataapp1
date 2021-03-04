from django.contrib import admin
from djangoApp.models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.conf.urls import *
from .forms import *
from django.template.response import TemplateResponse
import csv
from django.http import HttpResponse
from django.urls import path

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

@admin.register(Microenterpreneur)
class MicroenterpreneurAdmin(admin.ModelAdmin, ExportCsvMixin):
    change_list_template = "entities/microenterpreneurs_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('csv-import/', self.csv_import),
            path('csv-update/', self.csv_update),
        ]
        return my_urls + urls

    def csv_update(self, request):
        if request.method == "POST":
            Microenterpreneur.objects.all().delete()
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                print("File is not CSV type")
                # messages.error(request,'File is not CSV type')
                # return HttpResponseRedirect(reverse("myapp:upload_csv"))

            file_data = csv_file.read().decode("utf-8")     

            lines = file_data.split("\n")
            print("LINES : ",lines)
            for line in lines:                      
                fields = line.split(",")
                print(fields)
                data_dict = {}
                data_dict["microenterpreneur_name"] = fields[0]
                if fields[1] == '1':
                    data_dict["is_active"] = True
                else:
                    data_dict["is_active"] = False
                data_dict["mobile"] = fields[2]
                data_dict["email"] = fields[3]
                data_dict["name"] = fields[4]
                data_dict["address_line1"] = fields[5]
                data_dict["address_line2"] = fields[6]
                data_dict["city"] = fields[7]
                data_dict["state"] = fields[8]
                data_dict["pincode"] = fields[9]
                data_dict["geolocation"] = fields[10]

                Microenterpreneur(microenterpreneur_name=data_dict["microenterpreneur_name"],is_active=data_dict["is_active"],mobile=data_dict["mobile"],email=data_dict["email"],name=data_dict["name"],address_line1=data_dict["address_line1"],address_line2=data_dict["address_line2"],city_id=data_dict["city"],state_id=data_dict["state"],pincode=data_dict["pincode"],geolocation=data_dict["geolocation"]).save()

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

    def csv_import(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                print("File is not CSV type")
                # messages.error(request,'File is not CSV type')
                # return HttpResponseRedirect(reverse("myapp:upload_csv"))

            file_data = csv_file.read().decode("utf-8")     

            lines = file_data.split("\n")
            print("LINES : ",lines)
            for line in lines:                      
                fields = line.split(",")
                print(fields)
                data_dict = {}
                data_dict["microenterpreneur_name"] = fields[0]
                if fields[1] == 'yes':
                    data_dict["is_active"] = True
                elif fields[1] == 'yes':
                    data_dict["is_active"] = False
                else:
                    data_dict["is_active"] = True

                data_dict["mobile"] = fields[2]
                data_dict["email"] = fields[3]
                data_dict["name"] = fields[4]
                data_dict["address_line1"] = fields[5]
                data_dict["address_line2"] = fields[6]
                data_dict["city"] = fields[7]
                data_dict["state"] = fields[8]
                data_dict["pincode"] = fields[9]
                data_dict["geolocation"] = fields[10]

                Microenterpreneur(microenterpreneur_name=data_dict["microenterpreneur_name"],is_active=data_dict["is_active"],mobile=data_dict["mobile"],email=data_dict["email"],name=data_dict["name"],address_line1=data_dict["address_line1"],address_line2=data_dict["address_line2"],city_id=data_dict["city"],state_id=data_dict["state"],pincode=data_dict["pincode"],geolocation=data_dict["geolocation"]).save()

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

    list_display = ('id', 'microenterpreneur_name', 'is_active', 'mobile', 'email')
    fieldsets = (
    ('Microenterpreneur', {
        'fields': ('microenterpreneur_name', 'is_active', 'mobile', 'email')
    }),
    ('Address', {
        'fields': ('name', 'address_line1', 'address_line2', 'city', 'state','pincode', 'geolocation'),
    }),
    )

    def address(self,obj):
        return ', '.join([obj.name, obj.address_line1, obj.address_line2, obj.city.name, obj.state.name, str(obj.pincode), obj.geolocation])


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin,ExportCsvMixin):
    change_list_template = "entities/manufacturers_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('csv-import/', self.csv_import),
            path('csv-update/', self.csv_update),
        ]
        return my_urls + urls

    def csv_update(self, request):
        if request.method == "POST":
            Manufacturer.objects.all().delete()
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                print("File is not CSV type")
                # messages.error(request,'File is not CSV type')
                # return HttpResponseRedirect(reverse("myapp:upload_csv"))

            file_data = csv_file.read().decode("utf-8")     

            lines = file_data.split("\n")

            for line in lines[1:]:                      
                fields = line.split(",")
                print(fields)
                data_dict = {}
                data_dict["name"] = fields[0]
                if fields[1] == 'yes':
                    data_dict["is_active"] = True
                elif fields[1] == 'no':
                    data_dict["is_active"] = False
                else:
                    data_dict["is_active"] = True
                

                Manufacturer(name=data_dict["name"],is_active=data_dict["is_active"]).save()

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

    def csv_import(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                print("File is not CSV type")
                # messages.error(request,'File is not CSV type')
                # return HttpResponseRedirect(reverse("myapp:upload_csv"))

            file_data = csv_file.read().decode("utf-8")     

            lines = file_data.split("\n")

            for line in lines[1:]:                      
                fields = line.split(",")
                print(fields)
                data_dict = {}
                data_dict["name"] = fields[0]
                if fields[1] == 'yes':
                    data_dict["is_active"] = True
                elif fields[1] == 'no':
                    data_dict["is_active"] = False
                else:
                    data_dict["is_active"] = True
                

                Manufacturer(name=data_dict["name"],is_active=data_dict["is_active"]).save()

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )
    list_display = ('id','name', 'is_active')


# @admin.register(City)
# class CityAdmin(ImportExportModelAdmin):
#     list_display = ('id','name','state')

# @admin.register(State)
# class StateAdmin(ImportExportModelAdmin):
#     list_display = ('id','name')



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin,ExportCsvMixin):
    change_list_template = "entities/brands_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('csv-import/', self.csv_import),
            path('csv-update/', self.csv_update),
        ]
        return my_urls + urls

    def csv_update(self, request):
        if request.method == "POST":
            Brand.objects.all().delete()
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                print("File is not CSV type")
                # messages.error(request,'File is not CSV type')
                # return HttpResponseRedirect(reverse("myapp:upload_csv"))

            file_data = csv_file.read().decode("utf-8")     

            lines = file_data.split("\n")

            for line in lines[1:]:                      
                fields = line.split(",")
                print(fields)
                data_dict = {}
                data_dict["name"] = fields[0]
                data_dict["fk_manufacturer"] = fields[1]
                if fields[2] == 'yes':
                    data_dict["is_active"] = True
                elif fields[2] == 'no':
                    data_dict["is_active"] = False
                else:
                    data_dict["is_active"] = True
                data_dict["image_link"] = fields[3]
                                
                Brand(name=data_dict["name"],fk_manufacturer_id=data_dict["fk_manufacturer"],is_active=data_dict["is_active"],image_link=data_dict["image_link"]).save()

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "admin/csv_form.html", payload)


    def csv_import(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                print("File is not CSV type")
                # messages.error(request,'File is not CSV type')
                # return HttpResponseRedirect(reverse("myapp:upload_csv"))

            file_data = csv_file.read().decode("utf-8")     

            lines = file_data.split("\n")

            for line in lines[1:]:                      
                fields = line.split(",")
                print(fields)
                data_dict = {}
                data_dict["name"] = fields[0]
                data_dict["fk_manufacturer"] = fields[1]
                if fields[2] == 'yes':
                    data_dict["is_active"] = True
                elif fields[2] == 'no':
                    data_dict["is_active"] = False
                else:
                    data_dict["is_active"] = True
                data_dict["image_link"] = fields[3]
                                
                Brand(name=data_dict["name"],fk_manufacturer_id=data_dict["fk_manufacturer"],is_active=data_dict["is_active"],image_link=data_dict["image_link"]).save()

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "admin/csv_form.html", payload)


    list_display = (
        'id', 'name', 'fk_manufacturer', 'is_active', 'image_link')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin,ExportCsvMixin):
    change_list_template = "entities/categorys_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('csv-import/', self.csv_import),
            path('csv-update/', self.csv_update),
        ]
        return my_urls + urls

    def csv_update(self, request):
        if request.method == "POST":
            Category.objects.all().delete()
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                print("File is not CSV type")
                # messages.error(request,'File is not CSV type')
                # return HttpResponseRedirect(reverse("myapp:upload_csv"))

            file_data = csv_file.read().decode("utf-8")     

            lines = file_data.split("\n")

            for line in lines[1:]:                      
                fields = line.split(",")
                print(fields)
                data_dict = {}
                data_dict["name"] = fields[0]
                if fields[1] == '' or fields[1] == 'null':
                    data_dict["fk_parent_category"] = 0
                else:
                    data_dict["fk_parent_category"] = fields[1]

                if fields[2] == 'yes':
                    data_dict["is_active"] = True
                elif fields[2] == 'no':
                    data_dict["is_active"] = False
                else:
                    data_dict["is_active"] = True
                data_dict["image_link"] = fields[3]
                                

                Category(name=data_dict["name"],fk_parent_category=data_dict["fk_parent_category"],is_active=data_dict["is_active"],image_link=data_dict["image_link"]).save()

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "admin/csv_form.html", payload)

    def csv_import(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                print("File is not CSV type")
                # messages.error(request,'File is not CSV type')
                # return HttpResponseRedirect(reverse("myapp:upload_csv"))

            file_data = csv_file.read().decode("utf-8")     

            lines = file_data.split("\n")

            for line in lines[1:]:                      
                fields = line.split(",")
                print(fields)
                data_dict = {}
                data_dict["name"] = fields[0]
                if fields[1] == '' or fields[1] == 'null':
                    data_dict["fk_parent_category"] = 0
                else:
                    data_dict["fk_parent_category"] = fields[1]

                if fields[2] == 'yes':
                    data_dict["is_active"] = True
                elif fields[2] == 'no':
                    data_dict["is_active"] = False
                else:
                    data_dict["is_active"] = True
                data_dict["image_link"] = fields[3]
                

                Category(name=data_dict["name"],fk_parent_category=data_dict["fk_parent_category"],is_active=data_dict["is_active"],image_link=data_dict["image_link"]).save()


            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

    list_display = ('id', 'name', 'fk_parent_category', 'is_active', 'image_link')


class ProductBarCodeAdmin(admin.TabularInline):
    # list_display = ('id', 'barcode', 'fk_product', 'is_active')
    model = ProductBarCode

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin,ExportCsvMixin):
    change_list_template = "entities/products_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('csv-import/', self.csv_import),
            path('csv-update/', self.csv_update),
        ]
        return my_urls + urls

    def csv_update(self, request):
        if request.method == "POST":
            Product.objects.all().delete()
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                print("File is not CSV type")
                # messages.error(request,'File is not CSV type')
                # return HttpResponseRedirect(reverse("myapp:upload_csv"))

            file_data = csv_file.read().decode("utf-8")     

            lines = file_data.split("\n")

            for line in lines[1:]:                      
                fields = line.split(",")
                print(fields)
                data_dict = {}
                data_dict["name"] = fields[0]
                data_dict["article_code"] = fields[1]
                data_dict["fk_category"] = fields[2]
                data_dict["fk_brand"] = fields[3]
                data_dict["pack_qty"] = fields[4]
                data_dict["metric_unit"] = fields[5]
                data_dict["uom"] = fields[6]
                data_dict["pack_site"] = fields[7]
                data_dict["pack_type"] = fields[8]

                if fields[9] == 'yes':
                    data_dict["is_active"] = True
                elif fields[9] == 'no':
                    data_dict["is_active"] = False
                else:
                    data_dict["is_active"] = True

                if fields[10] == 'yes':
                    data_dict["is_online"] = True
                elif fields[10] == 'no':
                    data_dict["is_online"] = False
                else:
                    data_dict["is_online"] = True

                if fields[11] == 'yes':
                    data_dict["is_expirable"] = True
                elif fields[11] == 'no':
                    data_dict["is_expirable"] = False
                else:
                    data_dict["is_expirable"] = False

                Product(name=data_dict["name"],article_code=data_dict["article_code"],fk_category_id=data_dict["fk_category"],fk_brand_id=data_dict["fk_brand"],pack_qty=data_dict["pack_qty"],metric_unit=data_dict["metric_unit"],uom=   data_dict["uom"],pack_site=data_dict["pack_site"],pack_type=data_dict["pack_type"],is_active=data_dict["is_active"],is_online=data_dict["is_online"],is_expirable=data_dict["is_expirable"]).save()

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

    def csv_import(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                print("File is not CSV type")
                # messages.error(request,'File is not CSV type')
                # return HttpResponseRedirect(reverse("myapp:upload_csv"))

            file_data = csv_file.read().decode("utf-8")     

            lines = file_data.split("\n")
           
            for line in lines[1:]:                      
                fields = line.split(",")
                print(fields)
                data_dict = {}
                data_dict["name"] = fields[0]
                data_dict["article_code"] = fields[1]
                data_dict["fk_category"] = fields[2]
                data_dict["fk_brand"] = fields[3]
                data_dict["pack_qty"] = fields[4]
                data_dict["metric_unit"] = fields[5]
                data_dict["uom"] = fields[6]
                data_dict["pack_site"] = fields[7]
                data_dict["pack_type"] = fields[8]

                if fields[9] == 'yes':
                    data_dict["is_active"] = True
                elif fields[9] == 'no':
                    data_dict["is_active"] = False
                else:
                    data_dict["is_active"] = True

                if fields[10] == 'yes':
                    data_dict["is_online"] = True
                elif fields[10] == 'no':
                    data_dict["is_online"] = False
                else:
                    data_dict["is_online"] = True

                if fields[11] == 'yes':
                    data_dict["is_expirable"] = True
                elif fields[11] == 'no':
                    data_dict["is_expirable"] = False
                else:
                    data_dict["is_expirable"] = False

                print(data_dict)
                Product(name=data_dict["name"],article_code=data_dict["article_code"],fk_category_id=data_dict["fk_category"],fk_brand_id=data_dict["fk_brand"],pack_qty=data_dict["pack_qty"],metric_unit=data_dict["metric_unit"],uom=   data_dict["uom"],pack_site=data_dict["pack_site"],pack_type=data_dict["pack_type"],is_active=data_dict["is_active"],is_online=data_dict["is_online"],is_expirable=data_dict["is_expirable"]).save()
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )
    list_display = (
        'id', 'name', 'article_code', 'fk_category', 'fk_brand', 'pack_qty',
        'metric_unit', 'uom', 'pack_site', 'pack_type', 'is_active',
        'is_online',
        'is_expirable')
    inlines = [ProductBarCodeAdmin]


# class CustomerAddressInline(admin.StackedInline):
#     model = Customer
#     extra = 1

# @admin.register(Address)
# class AddressAdmin(ImportExportModelAdmin):
#     list_display = ('id', 'name', 'address_line1', 'address_line2', 'city', 'state','pincode', 'geolocation')
#     inlines = [CustomerAddressInline]

@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'mobile', 'credit', 'loyalty_point',
        'wallet_amount','address')
    
    fieldsets = (
        ('Customer', {
            'fields': ('customer_name', 'mobile', 'credit', 'loyalty_point',
        'wallet_amount')
        }),
        ('Address', {
            'fields': ('name', 'address_line1', 'address_line2', 'city', 'state','pincode', 'geolocation'),
        }),
    )

    def address(self,obj):
        return ', '.join([obj.name, obj.address_line1, obj.address_line2, obj.city.name, obj.state.name, str(obj.pincode), obj.geolocation])




@admin.register(Store)
class StoreAdmin(ImportExportModelAdmin):
    list_display = ('id', 'store_name',  'fk_microenterpreneur','store_code')
    
    fieldsets = (
        ('Store', {
            'fields': ('store_name',  'fk_microenterpreneur','store_code')
        }),
        ('Address', {
            'fields': ('name', 'address_line1', 'address_line2', 'city', 'state','pincode', 'geolocation'),
        }),
    )

    def address(self,obj):
        return ', '.join([obj.name, obj.address_line1, obj.address_line2, obj.city.name, obj.state.name, str(obj.pincode), obj.geolocation])

# @admin.register(Microenterpreneur)
# class MicroenterpreneurAdmin(ImportExportModelAdmin):
#     list_display = (
#         'id', 'name', 'is_active', 'mobile', 'email')


# @admin.register(Store)
# class StoreAdmin(ImportExportModelAdmin):
#     list_display = ('id', 'name',  'fk_microenterpreneur')

    # def has_add_permission(self, request, obj=None):
    #     return False



@admin.register(StoreAssortment)
class StoreAssortmentAdmin(ImportExportModelAdmin,ExportCsvMixin):
    change_list_template = "entities/storeAssortments_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('csv-import/', self.csv_import),
            path('csv-update/', self.csv_update),
        ]
        return my_urls + urls

    def csv_update(self, request):
        if request.method == "POST":
            StoreAssortment.objects.all().delete()
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                print("File is not CSV type")
                # messages.error(request,'File is not CSV type')
                # return HttpResponseRedirect(reverse("myapp:upload_csv"))

            file_data = csv_file.read().decode("utf-8")     

            lines = file_data.split("\n")

            for line in lines[1:]:                      
                fields = line.split(",")
                print(fields)
                data_dict = {}
                data_dict["fk_store"] = fields[0]
                data_dict["fk_product"] = fields[1]
                if fields[2] == 'yes':
                    data_dict["is_active"] = True
                elif fields[2] == 'no':
                    data_dict["is_active"] = False
                else:
                    data_dict["is_active"] = True
                data_dict["min_qty"] = fields[3]
                data_dict["max_qty"] = fields[4]
                data_dict["sp"] = fields[5]

                StoreAssortment(fk_store_id=data_dict["fk_store"],fk_product_id=data_dict["fk_product"],is_active=data_dict["is_active"],min_qty=data_dict["min_qty"],max_qty=data_dict["max_qty"],sp=data_dict["sp"]).save()

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

    def csv_import(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                print("File is not CSV type")
                # messages.error(request,'File is not CSV type')
                # return HttpResponseRedirect(reverse("myapp:upload_csv"))

            file_data = csv_file.read().decode("utf-8")     

            lines = file_data.split("\n")
           

            for line in lines[1:]:                      
                fields = line.split(",")
                print(fields)
                data_dict = {}
                data_dict["fk_store"] = fields[0]
                data_dict["fk_product"] = fields[1]
                if fields[2] == 'yes':
                    data_dict["is_active"] = True
                elif fields[2] == 'no':
                    data_dict["is_active"] = False
                else:
                    data_dict["is_active"] = True
                data_dict["min_qty"] = fields[3]
                data_dict["max_qty"] = fields[4]
                data_dict["sp"] = fields[5]

                StoreAssortment(fk_store_id=data_dict["fk_store"],fk_product_id=data_dict["fk_product"],is_active=data_dict["is_active"],min_qty=data_dict["min_qty"],max_qty=data_dict["max_qty"],sp=data_dict["sp"]).save()

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )
    list_display = (
        'id', 'fk_store', 'fk_product', 'is_active', 'min_qty', 'max_qty',
        'sp')


@admin.register(StoreInventory)
class StoreInventoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'fk_store', 'fk_product', 'mrp', 'quantity')


@admin.register(StoreInventoryTransactions)
class StoreInventoryTransactionsAdmin(admin.ModelAdmin,ExportCsvMixin):
    change_list_template = "entities/storeInventoryTransactionss_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('csv-import/', self.csv_import),
            path('csv-update/', self.csv_update),
        ]
        return my_urls + urls

    def csv_update(self, request):
        if request.method == "POST":
            StoreInventoryTransactions.objects.all().delete()
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                print("File is not CSV type")
                # messages.error(request,'File is not CSV type')
                # return HttpResponseRedirect(reverse("myapp:upload_csv"))

            file_data = csv_file.read().decode("utf-8")     

            lines = file_data.split("\n")

            for line in lines[1:]:                      
                fields = line.split(",")
                print(fields)
                data_dict = {}
                data_dict["fk_store"] = int(fields[0])
                data_dict["fk_product"] = int(fields[1])
                data_dict["fk_barcode"] = fields[2]
                data_dict["mrp"] = fields[3]
                data_dict["expiry_date"] = fields[4]
                data_dict["batch_number"] = fields[5]
                data_dict["txn_type"] = fields[6]
                data_dict["reference_number"] = fields[7]
                data_dict["quantity"] = int(fields[8])
                data_dict["comment"] = fields[9]

                print(data_dict)

                store_obj = Store.objects.get(id=data_dict["fk_store"])
                product_obj = Product.objects.filter(id=data_dict["fk_product"])

                if data_dict["txn_type"] == 'stock_transfer':
                    qty = product_obj[0].pack_qty - data_dict["quantity"]
                elif data_dict["txn_type"] == 'stock_return':
                    qty = product_obj[0].pack_qty + data_dict["quantity"]
                elif data_dict["txn_type"] == 'local_purchase':
                    qty = product_obj[0].pack_qty - data_dict["quantity"]
                elif data_dict["txn_type"] == 'stock_audit_adjustment':
                    qty = product_obj[0].pack_qty - data_dict["quantity"]
                elif data_dict["txn_type"] == 'pos_returns':
                    qty = product_obj[0].pack_qty - data_dict["quantity"]
    
                product_obj.update(pack_qty=qty)

                store_inventory_obj = StoreInventory.objects.filter(fk_store_id=data_dict["fk_store"],fk_product=data_dict["fk_product"])
                if store_inventory_obj:
                    store_inventory_obj.update(mrp=data_dict["mrp"],quantity=qty)
                else:
                    StoreInventory(fk_store_id=data_dict["fk_store"],fk_product_id=data_dict["fk_product"],mrp=data_dict["mrp"],quantity=qty).save()   


                StoreInventoryTransactions(fk_store_id=data_dict["fk_store"],fk_product_id=data_dict["fk_product"],fk_barcode_id=data_dict["fk_barcode"],mrp=data_dict["mrp"],expiry_date=data_dict["expiry_date"],batch_number=data_dict["batch_number"],txn_type=data_dict["txn_type"],reference_number=data_dict["reference_number"],quantity=data_dict["quantity"],comment=data_dict["comment"]).save()
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

    def csv_import(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                print("File is not CSV type")
                # messages.error(request,'File is not CSV type')
                # return HttpResponseRedirect(reverse("myapp:upload_csv"))

            file_data = csv_file.read().decode("utf-8")     

            lines = file_data.split("\n")

            for line in lines[1:]:                      
                fields = line.split(",")
                print(fields)
                data_dict = {}
                data_dict["fk_store"] = int(fields[0])
                data_dict["fk_product"] = int(fields[1])
                data_dict["fk_barcode"] = fields[2]
                data_dict["mrp"] = fields[3]
                data_dict["expiry_date"] = fields[4]
                data_dict["batch_number"] = fields[5]
                data_dict["txn_type"] = fields[6]
                data_dict["reference_number"] = fields[7]
                data_dict["quantity"] = int(fields[8])
                data_dict["comment"] = fields[9]

                print(data_dict)

                store_obj = Store.objects.get(id=data_dict["fk_store"])
                product_obj = Product.objects.filter(id=data_dict["fk_product"])

                if data_dict["txn_type"] == 'stock_transfer':
                    qty = product_obj[0].pack_qty - data_dict["quantity"]
                elif data_dict["txn_type"] == 'stock_return':
                    qty = product_obj[0].pack_qty + data_dict["quantity"]
                elif data_dict["txn_type"] == 'local_purchase':
                    qty = product_obj[0].pack_qty - data_dict["quantity"]
                elif data_dict["txn_type"] == 'stock_audit_adjustment':
                    qty = product_obj[0].pack_qty - data_dict["quantity"]
                elif data_dict["txn_type"] == 'pos_returns':
                    qty = product_obj[0].pack_qty - data_dict["quantity"]
    
                product_obj.update(pack_qty=qty)

                store_inventory_obj = StoreInventory.objects.filter(fk_store_id=data_dict["fk_store"],fk_product=data_dict["fk_product"])
                if store_inventory_obj:
                    store_inventory_obj.update(mrp=data_dict["mrp"],quantity=qty)
                else:
                    StoreInventory(fk_store_id=data_dict["fk_store"],fk_product_id=data_dict["fk_product"],mrp=data_dict["mrp"],quantity=qty).save()   


                StoreInventoryTransactions(fk_store_id=data_dict["fk_store"],fk_product_id=data_dict["fk_product"],fk_barcode_id=data_dict["fk_barcode"],mrp=data_dict["mrp"],expiry_date=data_dict["expiry_date"],batch_number=data_dict["batch_number"],txn_type=data_dict["txn_type"],reference_number=data_dict["reference_number"],quantity=data_dict["quantity"],comment=data_dict["comment"]).save()

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

    list_display = ('id', 'fk_store', 'fk_product', 'fk_barcode', 'mrp',
                    'expiry_date', 'batch_number', 'txn_type',
                    'reference_number', 'quantity', 'comment')


# class StoreCheckOutItemsAdmin(admin.TabularInline):
#     # list_display = ('id', 'fk_store_checkout', 'fk_product', 'qty', 'mrp',
#     #                 'sp', 'attributed_cart_discount')
#     extra = 1
#     model = StoreCheckOutItems

class StoreCheckOutItemsAdmin(admin.TabularInline):
    extra = 0
    model = StoreCheckOutItems
    readonly_fields = ('fk_store_checkout', 'fk_product', 'qty', 'mrp','sp', 'attributed_cart_discount')


@admin.register(StoreCheckout)
class StoreCheckoutAdmin(ImportExportModelAdmin):
    list_display = ('id','date', 'invoice_number', 'fk_store', 'fk_customer',
                    'is_delivery', 'is_online', 'promotions',
                    'cast_discount', 'sub_total', 'grand_total', 'payments',
                    'loyalty_point_used', 'wallet_amount_used')
    inlines = [ StoreCheckOutItemsAdmin]
    readonly_fields = ('date', 'invoice_number', 'fk_store', 'fk_customer','is_delivery', 'is_online', 'promotions','cast_discount', 'sub_total', 'grand_total', 'payments','loyalty_point_used', 'wallet_amount_used')


class StocktransferItemsAdmin(admin.TabularInline):
    # list_display = ('id', 'fk_stock_transfer', 'fk_product', 'mrp',
    #                 'expiry_date', 'quantity')
    extra = 0
    model = StocktransferItems
    readonly_fields = ('fk_stock_transfer', 'fk_product', 'mrp',
                    'expiry_date', 'quantity')

@admin.register(StockTransfer)
class StockTransferAdmin(ImportExportModelAdmin):
    list_display = ('id', 'date', 'order_number', 'sales_invoice_number',
                    'fk_store')
    inlines = [ StocktransferItemsAdmin ]
    readonly_fields = ('date', 'order_number', 'sales_invoice_number',
                    'fk_store')

@admin.register(Warehouse)
class WarehouseAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name',  'is_active', 'warehouse_code')


# admin.site.disable_action('delete_selected')