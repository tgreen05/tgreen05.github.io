from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator

from django.contrib import messages

from .forms import UploadForm, CreateUserForm
from .models import UploadFile


# Create your views here.
def registerUser(request):
	form = CreateUserForm()
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == "POST":
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('login')
			else:
				
				messages.info(request, 'wajib di isi!!!')
	
	context = {'form':form}
	return render(request, 'tgreen/form_register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == "POST":
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')

			else:
				messages.error(request, 'username atau password salah!!!')
			
		return render(request, 'tgreen/form_login.html')


def logOut(request):
	logout(request)
	return redirect('login')
	

@login_required(login_url='login')
def home(request):

	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			instance = UploadFile(file=request.FILES['file'], nama_file=request.POST['nama_file'])
			instance.save()
			messages.success(request, 'Berhasil di Upload')

		return redirect('/')
	else:
		form = UploadForm()

	return render(request, 'tgreen/index.html', {'form':form})


@login_required(login_url='login')
def download(request):
	if 'searchfile' in request.GET:
		searchfile = request.GET['searchfile']
		download = UploadFile.objects.filter(nama_file__icontains=searchfile)
	else:
		download = UploadFile.objects.all()


	paginator = Paginator(download, 5)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context={'download':download,
			 'page_obj':page_obj}
	return render(request, 'tgreen/download.html',context)

@login_required(login_url='login')
def updateFile(request, pk):
	update = UploadFile.objects.get(id=pk)
	form = UploadForm(instance=update)

	if request.method == 'POST':
		form = UploadForm(request.POST, instance=update)
		if form.is_valid():
			form.save()
			messages.success(request,'Update Berhasil.....')
		return redirect('download')

	context = {'form':form}
	return render(request, 'tgreen/form_update.html',context)

@login_required(login_url='login')
def deleteFile(request, pk):
	delete = UploadFile.objects.get(id=pk)
	delete.delete()
	messages.success(request,'Delete Berhasil.....')
	return redirect('download')

