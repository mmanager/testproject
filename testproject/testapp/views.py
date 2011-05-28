# -*- coding:utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import InfoRecord, RequestStore

def startpage(request):
	"""
		View for startpage
	"""
	info = get_object_or_404(InfoRecord, pk=1)
	
	return render_to_response('testapp/index.html', 
						{'info': info,
						}, context_instance=RequestContext(request)
	)
	
def handler404(request):
	"""
		Sample 404-error handler
	"""
	return render_to_response('404.html',
						{
						}, context_instance=RequestContext(request)
	)
	
def handler500(request):
	"""
		Sample 50x error handler
	"""
	return render_to_response('500.html',
						{
						}, context_instance=RequestContext(request)
	)
	

def show_last_requests(request):
	"""
		View that show last 10 stored requests
	"""
	requests = RequestStore.objects.all().order_by('-req_date')[:10]
	return render_to_response('testapp/requests.html',
						{'requests': requests,
						}, context_instance=RequestContext(request)
	)
