# -*- coding:utf-8 -*-
# Create your views here.
from django.contrib import admin 

from models import InfoRecord, RequestStore, DatabaseLog

class RequestStoreOptions(admin.ModelAdmin):
	list_filter = ('req_priority', )
	list_display = ('req_priority', 'req_date', 'req_method', 'req_path')

admin.site.register(InfoRecord)
admin.site.register(RequestStore, RequestStoreOptions)
admin.site.register(DatabaseLog)