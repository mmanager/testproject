# -*- coding:utf-8 -*-
from django import forms

from models import InfoRecord

class StartpageEditForm(forms.ModelForm):
	"""
		Edit startpage data form
	"""
	class Meta(object):
		model = InfoRecord