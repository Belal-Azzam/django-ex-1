from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
def index(request):
	return HttpResponse("<em>my second app </em>")
	
def help(request):
	my_dict = {'data':'bs yad'}
	return render(request,'AppTwo\index.html',my_dict)
# Create your views here.
def users(request):
	users = User.objects.all()
	data_dict = {'users':users}
	return render(request,'AppTwo\index.html',context=data_dict)