# -*- coding:utf-8 -*-
from django.utils.safestring import mark_safe
from django import forms
import testproject.settings as settings

class DatePickerWidget(forms.TextInput):
	"""
		widget for render jquery.ui datepicker
	"""
	def __init__(self, format, *args, **kwargs):
		super(DatePickerWidget, self).__init__(*args, **kwargs)
		self.format = format
		
	def render(self, name, value, attrs=None):
		format = self.format
		default = super(DatePickerWidget, self).render(name, value, attrs)
		if 'id' in attrs:
			id = attrs['id']
		else:
			id = 'id_%s' % name
		script = u'''
			<script type="text/javascript">
				$( "#%s" ).datepicker({'dateFormat': '%s'});
			</script>
		''' % (id, format)
		return mark_safe(u'%s\n%s' % (default, script))
		#return default