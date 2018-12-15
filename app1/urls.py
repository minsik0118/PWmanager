from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.mainpage),
	url(r'^account/',views.index),
	url(r'^account1/',views.login),
    url(r'^adduser/',views.adduser),
    url(r'^login1/',views.logintry),
    url(r'^login2/',views.record)
]
