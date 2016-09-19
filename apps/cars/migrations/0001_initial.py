# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Car'
        db.create_table(u'cars_car', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brand', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('construction', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('demonstration', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ez', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('mileage', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('power', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('transmission', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('main_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('photo_back', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('photo_wheel', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('photo_left', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('photo_right', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('photo_back_sit', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('photo_head', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('photo_rudder', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('photo_player', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('photo_door', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('photo_location', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('photo_info', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('photo_shop', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('photo_monitour', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('photo_advertisement', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'cars', ['Car'])


    def backwards(self, orm):
        # Deleting model 'Car'
        db.delete_table(u'cars_car')


    models = {
        u'cars.car': {
            'Meta': {'object_name': 'Car'},
            'brand': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'construction': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'demonstration': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ez': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mileage': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'photo_advertisement': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_back': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_back_sit': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_door': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_head': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_info': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_left': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_location': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_monitour': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_player': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_right': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_rudder': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_shop': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_wheel': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'power': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'transmission': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['cars']