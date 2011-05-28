# -*- coding:utf-8 -*-
import testproject.settings as settings

def add_settings_context_processor(request):
	return {'settings': settings}
