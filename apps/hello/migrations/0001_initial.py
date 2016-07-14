# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('jubber', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('bio', self.gf('django.db.models.fields.TextField')(default='')),
            ('other_contacts', self.gf('django.db.models.fields.TextField')()),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'hello', ['Person'])

        # Adding model 'Http_request'
        db.create_table('http_request', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('meth', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('query', self.gf('django.db.models.fields.TextField')(null=True)),
            ('is_read', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('status_code', self.gf('django.db.models.fields.CharField')(max_length=3, null=True)),
        ))
        db.send_create_signal(u'hello', ['Http_request'])

        # Adding model 'Entry'
        db.create_table(u'hello_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'hello', ['Entry'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('person')

        # Deleting model 'Http_request'
        db.delete_table('http_request')

        # Deleting model 'Entry'
        db.delete_table(u'hello_entry')


    models = {
        u'hello.entry': {
            'Meta': {'object_name': 'Entry'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'hello.http_request': {
            'Meta': {'ordering': "['-priority', '-date']", 'object_name': 'Http_request', 'db_table': "'http_request'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meth': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'path': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'query': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'status_code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'})
        },
        u'hello.person': {
            'Meta': {'object_name': 'Person', 'db_table': "'person'"},
            'bio': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jubber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['hello']