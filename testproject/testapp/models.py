# -*- coding:utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime


# Create your models here.

class InfoRecord(models.Model):
	"""
		This model contains basic info
	"""
	first_name = models.CharField(_(u'First Name'), max_length=100)
	last_name = models.CharField(_(u'Last Name'), max_length=100)
	birthdate = models.DateField(_(u'Date of Biarth'))	
	bio = models.TextField(_(u'Bio'))
	
	#contacts
	email = models.EmailField(_(u'Email'))
	jabber = models.CharField(_(u'Jabber ID'), max_length=255)
	skype = models.CharField(_(u'Skype'), max_length=255)
	other_contacts = models.TextField(_(u'Contacts'))
	
	class Meta(object):
		verbose_name = _(u'Info record')
		verbose_name_plural = _(u'Info records')
	
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class RequestStore(models.Model):
	"""
		This model contains all http requests
	"""
	req_date = models.DateTimeField(_(u'Request date'), default=datetime.datetime.now)
	req_method = models.CharField(_(u'Request method'), max_length=20)
	req_path = models.CharField(_(u'Request path'), max_length=255)
	
	class Meta(object):
		verbose_name = _(u'Request record')
		verbose_name_plural = _(u'Requests records')
	
	def __unicode__(self):
		return u'[%s] %s %s' % (self.req_date.strftime('%d.%m.%Y %H:%M:%S'), self.req_method, self.req_path)
	
	