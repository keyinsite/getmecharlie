from django.conf.urls import patterns, url
from charlie import views
from django.views.generic import TemplateView


urlpatterns = patterns('',
	url(r'^$', views.sign_up, name='sign_up'),
	url(r'sign-up/$', views.sign_up_info, name='sign_up_info'),
	url(r'payment/$', TemplateView.as_view(template_name='charlie/signup_payment.html'), name='payment'),
	)