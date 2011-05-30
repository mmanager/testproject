# -*- coding:utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('testapp.views', 
	url('^$', 'startpage', name='testapp_startpage'),
	url('^last-requests/$', 'show_last_requests', name='testapp-last_requests_page'),
	url('^edit-startpage/$', 'edit_startpage', name='testapp-edit-startpage'),
	url('^ajax-edit-startpage/$', 'ajax_edit_startpage', name='testapp-ajax-edit-startpage'),
)

urlpatterns += patterns('',
	url('^accounts/login', 'django.contrib.auth.views.login', name='testapp-login-page'),
	url('^accounts/logout', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='testapp-logout-page'),
)