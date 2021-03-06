# -*- coding:utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('testapp.views', 
	url('^$', 'startpage', name='testapp_startpage'),
	url('^last-requests/$', 'show_last_requests', name='testapp-last_requests_page'),
	url('^edit-startpage/$', 'edit_startpage', name='testapp-edit-startpage'),
	url('^ajax-edit-startpage/$', 'ajax_edit_startpage', name='testapp-ajax-edit-startpage'),
	url('^edit-startpage-reversed/$', 'edit_startpage_reversed', name='testapp-edit-startpage_reversed'),
	url('^ajax-edit-startpage-reversed/$', 'ajax_edit_startpage_reversed', name='testapp-ajax-edit-startpage_reversed'),
)

urlpatterns += patterns('',
	url('^accounts/login', 'django.contrib.auth.views.login', name='testapp-login-page'),
	url('^accounts/logout', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='testapp-logout-page'),
)