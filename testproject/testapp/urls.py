# -*- coding:utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('testapp.views', 
	url('^$', 'startpage', name='testapp_startpage'),
	url('^last-requests/$', 'show_last_requests', name='last_requests_page'),
)
