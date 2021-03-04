"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from djangoProject import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from djangoApp import views

app_name = 'djangoApp'
# sso_server = SsoServer()

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/account/', include('account.urls')),
    # path('api/accounts/', include('rest_registration.api.urls')),
    # path('api/', include('data.urls')),
    path('admin/', admin.site.urls),    
    # path('<int:manufacturer_id>/bust-cache',views.bust_manufacturer_cache,name='bust-manufacturer-cache'),
	path('store_inventory_transactions/',views.showIndex,name='main'),
	path('save_data/',views.saveData,name='save_data'),
	path('checkout/',views.checkout,name='checkout'),
	path('save_checkout/',views.saveCheckout,name='save_checkout'),
    path('store/',views.store,name='store'),
    path('add_store/',views.add_store,name='add_store'),
    path('update_address/',views.update_address,name='update_address'),
    path('save_address_update/',views.save_address_update,name='save_address_update'),
    path('delete_address/',views.delete_address,name='delete_address'),

    path('microenterpreneur/',views.microenterpreneur,name='microenterpreneur'),
    path('update_microenterpreneur_address/',views.update_microenterpreneur_address,name='update_microenterpreneur_address'),
    path('delete_microenterpreneur_address/',views.delete_microenterpreneur_address,name='delete_microenterpreneur_address'),
    path('save_microenterpreneur_address_update/',views.save_microenterpreneur_address_update,name='save_microenterpreneur_address_update'),
    path('add_microenterpreneur/',views.add_microenterpreneur,name='add_microenterpreneur'),

    path('customer/',views.customer,name='customer'),
    path('update_customer_address/',views.update_customer_address,name='update_customer_address'),
    path('delete_customer_address/',views.delete_customer_address,name='delete_customer_address'),
    path('save_customer_address_update/',views.save_customer_address_update,name='save_customer_address_update'),
    path('add_customer/',views.add_customer,name='add_customer'),

	path('storeInventoryTransactions/', views.storeInventoryTransactions,name='storeInventoryTransactions'),

]


# urlpatterns += [
#     path('api/server/', include(sso_server.get_urls())),
# ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)