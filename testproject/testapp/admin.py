# -*- coding:utf-8 -*-
# Create your views here.
from django.contrib import admin 

from models import InfoRecord, RequestStore, DatabaseLog

admin.site.register(InfoRecord)
admin.site.register(RequestStore)
admin.site.register(DatabaseLog)