# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'Banner.custom_html'
        db.add_column('banners_banner', 'custom_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Changing field 'Banner.image'
        db.alter_column('banners_banner', 'image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True))
    
    
    def backwards(self, orm):
        
        # Deleting field 'Banner.custom_html'
        db.delete_column('banners_banner', 'custom_html')

        # Changing field 'Banner.image'
        db.alter_column('banners_banner', 'image', self.gf('django.db.models.fields.files.FileField')(max_length=100))
    
    
    models = {
        'banners.banner': {
            'Meta': {'object_name': 'Banner'},
            'custom_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_rollover': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'popup': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'slot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['banners.Slot']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'banners.slot': {
            'Meta': {'object_name': 'Slot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rotate': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        }
    }
    
    complete_apps = ['banners']
