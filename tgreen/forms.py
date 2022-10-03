from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import UploadFile

class UploadForm(ModelForm):
	class Meta:

		model = UploadFile
		fields = ['nama_file','file']


		widgets ={

				'nama_file':forms.TextInput(attrs={'class':'form-control'}),


		} 


class CreateUserForm(UserCreationForm):

	password1 = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "type":"password"}))

	password2 = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "type":"password"}))

	class Meta:

		model = User
		fields = ['username','email','password1','password2']

		widgets ={

			  'username':forms.TextInput(attrs={"class":"form-control"}),
			  'email':forms.TextInput(attrs={"class":"form-control", "type":"email"}),
			  

		}




