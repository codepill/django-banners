
from south.db import db
from django.db import models
from banners.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Banner.title'
        db.add_column('banners_banner', 'title', orm['banners.banner:title'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Banner.title'
        db.delete_column('banners_banner', 'title')
        
    
    
    models = {
        'banners.banner': {
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'image_rollover': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'popup': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'slot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['banners.Slot']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'banners.slot': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rotate': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        }
    }
    
    complete_apps = ['banners']
