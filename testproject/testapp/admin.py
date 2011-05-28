# -*- coding:utf-8 -*-
# Create your views here.
from django.contrib import admin 

from models import InfoRecord, RequestStore

admin.site.register(InfoRecord)
admin.site.register(RequestStore)
