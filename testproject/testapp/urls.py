# -*- coding:utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('testapp.views', 
	url('^$', 'startpage', name='testapp_startpage'),
)
