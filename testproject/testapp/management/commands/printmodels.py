# -*- coding:utf-8 -*-
import sys
from django.core.management.base import BaseCommand, CommandError

from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
	"""
		This command print all models and count objects into there models
	"""
	def handle(self, *args, **options):
		for ct in ContentType.objects.all().order_by('app_label'):
			s = '%s -> %s Total:%d objects' % (ct.app_label, ct.model, ct.model_class().objects.all().count())
			print s
			print >> sys.stderr, 'error: %s' % s