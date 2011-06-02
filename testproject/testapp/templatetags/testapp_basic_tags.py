# -*- coding:utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.core import urlresolvers
from django import template


def get_object_params(content_object):
	"""
		This function "extract" app_label, model_name and id from given content_object
	"""
	ct = ContentType.objects.get_for_model(content_object)
	kwargs = {
		'app_label': ct.app_label,
		'model_name': ct.model,
		'object_id': getattr(content_object, 'pk', getattr(content_object, 'id')),
	}
	return kwargs

def edit_link(content_object):
	"""
		This function return admin edit url for given objects
	"""
	kwargs = get_object_params(content_object)
	return urlresolvers.reverse('admin:%(app_label)s_%(model_name)s_change'%kwargs, args=(kwargs['object_id'], ))

register = template.Library()
register.simple_tag(edit_link)