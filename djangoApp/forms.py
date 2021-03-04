from django import forms
from .models import *

# class UpdateMicroenterpreneurForm(forms.Form):
# 	file = forms.FileField(required=True,help_text="Please Select CSV File")
	


# class UpdateActionForm(forms.Form):
# 	file = forms.FileField(required=True)

# 	def form_action(self,upload,user):
# 		raise NotImplementedError()

# 	def save(self,upload,user):
# 		try:
# 			upload,action = self.form_action(upload,user)
# 		except errors.Error as e:
# 			print('error in form')
# 			error_message = str(e)
# 			self.add_error(None,error_message)
# 			raise
# 		if self.cleaned_data.get('file',False):
# 			return upload,action

# class UpdateForm(forms.Form):
# 	file = forms.FileField(required=True,help_text='Select CSV File')

# 	def form_action(self,upload,user):
# 		return Microenterpreneur.upload(id=upload.pk,user=upload.user,file=self.cleaned_data['file'])






class StoreInventoryTransactionsForm(forms.ModelForm):
	class Meta: 
		model = StoreInventoryTransactions
		fields = "__all__"

class StoreCheckoutForm(forms.ModelForm):
	class Meta: 
		model = StoreCheckout
		fields = "__all__"

class StoreCheckoutItemsForm(forms.ModelForm):
	class Meta:
		model = StoreCheckOutItems
		fields = "__all__"

