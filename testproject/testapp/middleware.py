# -*- coding:utf-8 -*-
from models import RequestStore
import pickle

class RequestStoreMiddleware(object):
	def process_request(self, request):
		store_obj = RequestStore.objects.create(req_method=request.method,
		                                                              req_path=request.path
		)
		return None