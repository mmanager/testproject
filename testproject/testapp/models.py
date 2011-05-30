# -*- coding:utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import smart_unicode

from django.db.models import signals
from django.dispatch import receiver


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
	
ADDITION = 1
CHANGE = 2
DELETION = 3

class DatabaseLogManager(models.Manager):
	def log_action(self,  content_type_id, object_id, object_repr, action_flag, change_message=''):
		e = self.model(None, None,  content_type_id, smart_unicode(object_id), object_repr[:200], action_flag, change_message)
		e.save()

class DatabaseLog(models.Model):
	"""
		Model store logs about changing any other models instances
	"""
	action_time = models.DateTimeField(_(u'action time'), auto_now=True)
	content_type = models.ForeignKey(ContentType, blank=True, null=True)
	object_id = models.TextField(_(u'object id'), blank=True, null=True)
	object_repr = models.CharField(_(u'object repr'), max_length=200)
	action_flag = models.PositiveSmallIntegerField(_(u'action flag'))
	change_message = models.TextField(_(u'change message'), blank=True)
	
	objects = DatabaseLogManager()
	
	class Meta(object):
		verbose_name = _(u'Database log record')
		verbose_name_plural = _(u'Database log records')
		ordering = ('-action_time', )
	
	def __repr__(self):
		return smart_unicode(self.action_time)
	
	def is_addition(self):
		return self.action_flag == ADDITION

	def is_change(self):
		return self.action_flag == CHANGE

	def is_deletion(self):
		return self.action_flag == DELETION
	
@receiver(signals.post_save)
def log_event(sender, *args, **kwargs):
	"""
		listen signal for store creation and edit events
	"""
	instance = kwargs['instance']
	ct = ContentType.objects.get_for_model(instance)
	if not isinstance(instance, DatabaseLog):
		if 'created' in kwargs:
			if kwargs['created']:
				DatabaseLog.objects.log_action(ct.pk, instance.pk, instance.__repr__(), 1)
			else:
				DatabaseLog.objects.log_action(ct.pk, instance.pk, instance.__repr__(), 2)
		else:
			DatabaseLog.objects.log_action(ct.pk, instance.pk, instance.__repr__(), 2)

@receiver(signals.post_delete)
def log_event(sender, *args, **kwargs):
	"""
		listen signal for store deleting event
	"""
	instance = kwargs['instance']
	ct = ContentType.objects.get_for_model(instance)
	if not isinstance(instance, DatabaseLog):
		DatabaseLog.objects.log_action(ct.pk, instance.pk, instance.__repr__(), 3)
	