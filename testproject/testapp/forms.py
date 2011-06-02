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