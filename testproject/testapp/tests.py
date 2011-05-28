# -*- coding:utf-8 -*-
from tddspry.django import DatabaseTestCase
from tddspry.django import HttpTestCase

import settings
from testproject.testapp.models import InfoRecord
import datetime

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
		
	def test_static(self):
		self.go(settings.MEDIA_URL)
		self.code(404)

		self.go(settings.MEDIA_URL + 'does_not_exist.exe')
		self.code(404)

		self.go(settings.MEDIA_URL + 'css/styles.css')
		self.code(200)		
