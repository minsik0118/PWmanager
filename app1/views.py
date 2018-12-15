from django.http import HttpResponse

from .models import webpage
from .models import member
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login



# Create your views here.
def index(request):
	loginid=request.POST['loginid']
	webpages= webpage.objects.filter(owner=loginid)
	context={'webpages':webpages, 'loginid':loginid}

	return render(request, 'app1/index.html',context)

def login(request):
	name=request.POST['name']
	loginid=request.POST['loginid']
	webpage1=webpage.objects.filter(name=name, owner=loginid)
	from selenium import webdriver
	import time
	username=webpage1[0].username
	password=webpage1[0].password
	url=webpage1[0].urls
	idid=webpage1[0].idid
	pwid=webpage1[0].pwid
	btid=webpage1[0].btid
	driver = webdriver.Chrome("C:/Users/minsi/Downloads/chromedriver_win32/chromedriver")

	driver.get(url)

	driver.find_element_by_id(idid).send_keys(username)
	driver.find_element_by_id(pwid).send_keys(password)
	try:
		driver.find_element_by_id(btid).click()
	except:
		driver.find_element_by_class_name(btid).click()
	webpages= webpage.objects.filter(owner=request.POST['loginid'])
	context={'webpages':webpages, 'loginid':loginid}

	return render(request, 'app1/index.html',context)

def adduser(request):
	return render(request, 'app1/adduser.html')

def mainpage(request):
	return render(request, 'app1/mainpage.html')

def logintry(request):
	try:
		loginid=request.POST['loginid']
		member1= member.objects.filter(memberid=loginid)
		name=member1[0].name

		return render(request, 'app1/voicerecord.html',{'name':name,'loginid':loginid})
	except:
		return render(request, 'app1/mainpage.html')
	return render(request, 'app1/voicerecord.html')

def record(request):

	webpages= webpage.objects.filter(owner=request.POST['loginid'])
	context={'webpages':webpages}

	return render(request, 'app1/index.html',context)