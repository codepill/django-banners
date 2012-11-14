# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Slot.rotate'
        db.delete_column('banners_slot', 'rotate')

        # Adding field 'Slot.language'
        db.add_column('banners_slot', 'language', self.gf('django.db.models.fields.CharField')(default='en', max_length=6), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Slot.rotate'
        db.add_column('banners_slot', 'rotate', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)

        # Deleting field 'Slot.language'
        db.delete_column('banners_slot', 'language')


    models = {
        'banners.banner': {
            'Meta': {'object_name': 'Banner'},
            'custom_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_rollover': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'popup': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['banners.Slot']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'banners.slot': {
            'Meta': {'object_name': 'Slot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '6'}),
            'limit': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'random': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'symbol': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        }
    }

    complete_apps = ['banners']
