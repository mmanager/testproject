# -*- coding:utf-8 -*-
from tddspry.django import DatabaseTestCase
from tddspry.django import HttpTestCase
from tddspry.django.helpers import *

from django.template import Context, Template
from django.contrib.contenttypes.models import ContentType


import settings
from testproject.testapp.models import InfoRecord, RequestStore, DatabaseLog, log_event, log_event_delete

import datetime



## Middleware tests
TEST_REQ_METHOD = 'POST'
TEST_REQ_PATH = '/media/css/styles.css'
NEW_TEST_REQ_METHOD = 'GET'

class TestMiddlewareReqDatabase(DatabaseTestCase):
	def test_create(self):
		req_record = self.assert_create(RequestStore,
								req_method=TEST_REQ_METHOD,
								req_path=TEST_REQ_PATH)
		self.assert_equal(req_record.req_method, TEST_REQ_METHOD)
		self.assert_equal(req_record.req_path, TEST_REQ_PATH)

	def test_delete(self):
		req_record = self.assert_create(RequestStore,
								req_method=TEST_REQ_METHOD,
								req_path=TEST_REQ_PATH)
		self.assert_delete(req_record)
	
	def test_read(self):
		req_record = self.assert_create(RequestStore,
								req_method=TEST_REQ_METHOD,
								req_path=TEST_REQ_PATH)
		self.assert_read(RequestStore, req_path=TEST_REQ_PATH)
	
	def test_update(self):
		req_record = self.assert_create(RequestStore,
								req_method=TEST_REQ_METHOD,
								req_path=TEST_REQ_PATH)
		self.assert_update(req_record, req_method=NEW_TEST_REQ_METHOD)

#####################

## Basic tests
TEST_FIRST_NAME = 'First'
TEST_LAST_NAME = 'Last'
TEST_BIO = 'Some bio'
TEST_BIRTH_DATE = datetime.date(1980, 1, 1)

TEST_EMAIL = 'email@domain.com'
TEST_JABBER = 'jid@jabber.org'
TEST_SKYPE = 'SKYPE'
TEST_OTHER_CONTACTS = 'Some contacts'

NEW_TEST_FIRST_NAME = 'New First Name'


class TestCustomDatabase(DatabaseTestCase):
	def test_create(self):
		record = self.assert_create(InfoRecord, 
							 first_name=TEST_FIRST_NAME,
							 last_name=TEST_LAST_NAME,
							 bio=TEST_BIO,
							 birthdate=TEST_BIRTH_DATE,
							 email=TEST_EMAIL,
							 jabber=TEST_JABBER,
							 skype=TEST_SKYPE,
							 other_contacts=TEST_OTHER_CONTACTS)
		
		self.assert_equal(record.first_name, TEST_FIRST_NAME)
		self.assert_equal(record.last_name, TEST_LAST_NAME)
		self.assert_equal(record.birthdate, TEST_BIRTH_DATE)
		self.assert_equal(record.bio, TEST_BIO)
		
		self.assert_equal(record.email, TEST_EMAIL)
		self.assert_equal(record.jabber, TEST_JABBER)
		self.assert_equal(record.skype, TEST_SKYPE)
		self.assert_equal(record.other_contacts, TEST_OTHER_CONTACTS)
		
		
	
	def test_delete(self):
		record = self.assert_create(InfoRecord, 
							 first_name=TEST_FIRST_NAME,
							 last_name=TEST_LAST_NAME,
							 bio=TEST_BIO,
							 birthdate=TEST_BIRTH_DATE,
							 email=TEST_EMAIL,
							 jabber=TEST_JABBER,
							 skype=TEST_SKYPE,
							 other_contacts=TEST_OTHER_CONTACTS)
		self.assert_delete(record)
	
	def test_read(self):
		record = self.assert_create(InfoRecord, 
							 first_name=TEST_FIRST_NAME,
							 last_name=TEST_LAST_NAME,
							 bio=TEST_BIO,
							 birthdate=TEST_BIRTH_DATE,
							 email=TEST_EMAIL,
							 jabber=TEST_JABBER,
							 skype=TEST_SKYPE,
							 other_contacts=TEST_OTHER_CONTACTS)
		self.assert_read(InfoRecord, first_name=TEST_FIRST_NAME)
	
	def test_update(self):
		record = self.assert_create(InfoRecord, 
							 first_name=TEST_FIRST_NAME,
							 last_name=TEST_LAST_NAME,
							 bio=TEST_BIO,
							 birthdate=TEST_BIRTH_DATE,
							 email=TEST_EMAIL,
							 jabber=TEST_JABBER,
							 skype=TEST_SKYPE,
							 other_contacts=TEST_OTHER_CONTACTS)
		self.assert_update(record, first_name=NEW_TEST_FIRST_NAME)




class TestHTTP(HttpTestCase):
	def test_index(self):
		self.go200('/')
		self.url('/')
		self.find('42 Coffee Cups Test Assignment')
	
	def test_last_requests(self):
		for i in xrange(10):
			path = '/path-%d/' % i
			record = RequestStore.objects.create(req_method='GET', req_path=path)
		
		self.go200('/last-requests/')
		resp = self.url('/last-requests/')
		self.find('/last-requests/')
		self.find('path-1')
		self.notfind('/path-0/')


	def test_static(self):
		self.go(settings.MEDIA_URL)
		self.code(404)

		self.go(settings.MEDIA_URL + 'does_not_exist.exe')
		self.code(404)

		self.go(settings.MEDIA_URL + 'css/styles.css')
		self.code(200)	
		
	def test_login(self):
		self.go200('/accounts/login')
		self.url('/accounts/login')
		
		self.login('admin', 'admin')
		self.go200('/')
		self.url('/')
		self.find('Logout')

	def test_logout(self):
		self.login('admin', 'admin')

		self.go200('/')
		self.find('Logout')

		self.logout()

		self.go200('/accounts/login')
		self.url('/accounts/login')
	
	def test_db_data_at_page(self):
		record = InfoRecord.objects.create(first_name=TEST_FIRST_NAME,
							 last_name=TEST_LAST_NAME,
							 bio=TEST_BIO,
							 birthdate=TEST_BIRTH_DATE,
							 email=TEST_EMAIL,
							 jabber=TEST_JABBER,
							 skype=TEST_SKYPE,
							 other_contacts=TEST_OTHER_CONTACTS
							 )
		self.go200('/')
		self.find(TEST_EMAIL)
		self.find(TEST_JABBER)
		
		
	#~ def test_form(self):
		#~ self.go200('/accounts/login')
		#~ self.url('/accounts/login')
		#~ self.login('admin', 'password')
		
		#~ self.go200('testapp-edit-startpage')
		#~ self.url('testapp-edit-startpage')
		#~ self.formvalue('edit-form', 'other_contacts', u'Testing other contacts')
		#~ self.submit200()
		#~ self.url('/')
		#~ self.find('Testing other contacts')



from django.test import TestCase

class TestContext(TestCase):
	def test_index(self):
		resp = self.client.get('/')
		self.assertTrue('settings' in resp.context)
		self.assertEqual(settings.MEDIA_URL, resp.context['settings'].MEDIA_URL)
	
	def test_db_data_in_context(self):
		record = InfoRecord.objects.create(first_name=TEST_FIRST_NAME,
							 last_name=TEST_LAST_NAME,
							 bio=TEST_BIO,
							 birthdate=TEST_BIRTH_DATE,
							 email=TEST_EMAIL,
							 jabber=TEST_JABBER,
							 skype=TEST_SKYPE,
							 other_contacts=TEST_OTHER_CONTACTS
							 )
		resp = self.client.get('/')
		self.assertTrue('info' in resp.context)
		self.assertEqual(resp.context['info'].email, TEST_EMAIL)

class TestCustomTemplateTags(TestCase):
	"""
		testing custom template tags
	"""
	def render_template(self, tmpl_text, context):
		t = Template(tmpl_text)
		return t.render(context)
		
	def test_admin_link_tag(self):
		tmpl = u'{% load testapp_basic_tags %}{% edit_link info %}'
		for i in xrange(10):
			record = InfoRecord.objects.create(first_name=TEST_FIRST_NAME,
								 last_name=TEST_LAST_NAME,
								 bio=TEST_BIO,
								 birthdate=TEST_BIRTH_DATE,
								 email=TEST_EMAIL,
								 jabber=TEST_JABBER,
								 skype=TEST_SKYPE,
								 other_contacts=TEST_OTHER_CONTACTS
								 )
			context = Context({'info': record})
			rendered  = self.render_template(tmpl, context)
			self.assertEqual(rendered, "/admin/testapp/inforecord/%d/"%record.pk)

class TestCustomSignalsProcessor(TestCase):
	"""
		Test custom signal processor for ticket #10
	"""
	def test_signals(self):
		record = InfoRecord.objects.create(first_name=TEST_FIRST_NAME,
							 last_name=TEST_LAST_NAME,
							 bio=TEST_BIO,
							 birthdate=TEST_BIRTH_DATE,
							 email=TEST_EMAIL,
							 jabber=TEST_JABBER,
							 skype=TEST_SKYPE,
							 other_contacts=TEST_OTHER_CONTACTS
							 )
		ct = ContentType.objects.get_for_model(record)
		
		## test add signal
		objects = DatabaseLog.objects.filter(content_type=ct, object_id=record.pk, action_flag=1)		
		self.assertTrue(objects.count() > 0)
		
		## test change signal
		objects = DatabaseLog.objects.filter(content_type=ct, object_id=record.pk, action_flag=2)		
		self.assertTrue(objects.count() == 0)
		record.first_name = NEW_TEST_FIRST_NAME
		record.save()
		objects = DatabaseLog.objects.filter(content_type=ct, object_id=record.pk, action_flag=2)		
		self.assertTrue(objects.count() > 0)
		
		## test delete signal
		pk = record.pk
		record.delete()
		objects = DatabaseLog.objects.filter(content_type=ct, object_id=pk, action_flag=3)
		self.assertTrue(objects.count() > 0)
		