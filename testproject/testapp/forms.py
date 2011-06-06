# -*- coding:utf-8 -*-
from django import forms

from models import InfoRecord
from widgets import DatePickerWidget

class StartpageEditForm(forms.ModelForm):
	"""
		Edit startpage data form
	"""
	class Meta(object):
		model = InfoRecord
		widgets = {
			'birthdate': DatePickerWidget(format='yy-mm-dd')
		}

class StartpageEditFormReversed(forms.ModelForm):
	"""
		Edit startpage data form
	"""
	class Meta(object):
		model = InfoRecord
		fields = ('bio', 'birthdate', 'last_name', 'first_name', 'other_contacts', 'skype', 'jabber', 'email')
		widgets = {
			'birthdate': DatePickerWidget(format='yy-mm-dd')
		}
