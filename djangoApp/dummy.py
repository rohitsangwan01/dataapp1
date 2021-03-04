
# @staff_member_required
# def upload(request):
#     # context = self.admin_site.each_context(request)
#     context = {}
#     context['form'] = UpdateMicroenterpreneurForm
#     return TemplateResponse(request,'admin/djangoApp/Microenterpreneur/change_form.html',context)
#     # return HttpResponseRedirect(request.META["HTTP_REFERER"])


# @admin.register(Microenterpreneur)
# class MicroenterpreneurAdmin(admin.ModelAdmin):
#     def get_urls(self):
#         urls = super(MicroenterpreneurAdmin,self).get_urls()
#         my_urls = [url(r"^update/$",upload)]
#         return my_urls + urls

#     list_display = ('id', 'microenterpreneur_name', 'is_active', 'mobile', 'email')
    
    # fieldsets = (
    #     ('Microenterpreneur', {
    #         'fields': ('microenterpreneur_name', 'is_active', 'mobile', 'email')
    #     }),
    #     ('Address', {
    #         'fields': ('name', 'address_line1', 'address_line2', 'city', 'state','pincode', 'geolocation'),
    #     }),
    # )

    # def address(self,obj):
    #     return ', '.join([obj.name, obj.address_line1, obj.address_line2, obj.city.name, obj.state.name, str(obj.pincode), obj.geolocation])


# @admin.register(Microenterpreneur)
# class MicroenterpreneurAdmin(admin.ModelAdmin):
#     def get_urls(self):
#         urls = super(MicroenterpreneurAdmin,self).get_urls()
#         my_urls = [url(r"^update/$",update)]
#         return my_urls + urls
#     list_display = ('id', 'name', 'is_active', 'mobile', 'email')

