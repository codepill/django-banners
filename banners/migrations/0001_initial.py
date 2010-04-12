
from south.db import db
from django.db import models
from banners.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Slot'
        db.create_table('banners_slot', (
            ('id', orm['banners.Slot:id']),
            ('name', orm['banners.Slot:name']),
        ))
        db.send_create_signal('banners', ['Slot'])
        
        # Adding model 'Banner'
        db.create_table('banners_banner', (
            ('id', orm['banners.Banner:id']),
            ('slot', orm['banners.Banner:slot']),
            ('image', orm['banners.Banner:image']),
        ))
        db.send_create_signal('banners', ['Banner'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Slot'
        db.delete_table('banners_slot')
        
        # Deleting model 'Banner'
        db.delete_table('banners_banner')
        
    
    
    models = {
        'banners.banner': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['banners.Slot']"})
        },
        'banners.slot': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }
    
    complete_apps = ['banners']
