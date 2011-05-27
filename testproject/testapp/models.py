# -*- coding:utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class InfoRecord(models.Model):
	"""
		This model contains basic info
	"""
	first_name = models.CharField(_(u'First Name'), max_length=100)
	last_name = models.CharField(_(u'Last Name'), max_length=100)
	bio = models.TextField(_(u'Bio'))
	contacts = models.TextField(_(u'Contacts'))
	
	class Meta(object):
		verbose_name = _(u'Info record')
		verbose_name_plural = _(u'Info records')
	
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)