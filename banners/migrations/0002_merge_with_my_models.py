
from south.db import db
from django.db import models
from banners.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Banner.popup'
        db.add_column('banners_banner', 'popup', orm['banners.banner:popup'])
        
        # Adding field 'Banner.image_rollover'
        db.add_column('banners_banner', 'image_rollover', orm['banners.banner:image_rollover'])
        
        # Adding field 'Banner.display_order'
        db.add_column('banners_banner', 'display_order', orm['banners.banner:display_order'])
        
        # Adding field 'Banner.destination'
        db.add_column('banners_banner', 'destination', orm['banners.banner:destination'])
        
        # Adding field 'Slot.limit'
        db.add_column('banners_slot', 'limit', orm['banners.slot:limit'])
        
        # Adding field 'Banner.is_published'
        db.add_column('banners_banner', 'is_published', orm['banners.banner:is_published'])
        
        # Adding field 'Slot.symbol'
        db.add_column('banners_slot', 'symbol', orm['banners.slot:symbol'])
        
        # Adding field 'Slot.rotate'
        db.add_column('banners_slot', 'rotate', orm['banners.slot:rotate'])
        
        # Changing field 'Banner.image'
        # (to signature: django.db.models.fields.files.FileField(max_length=100))
        db.alter_column('banners_banner', 'image', orm['banners.banner:image'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Banner.popup'
        db.delete_column('banners_banner', 'popup')
        
        # Deleting field 'Banner.image_rollover'
        db.delete_column('banners_banner', 'image_rollover')
        
        # Deleting field 'Banner.display_order'
        db.delete_column('banners_banner', 'display_order')
        
        # Deleting field 'Banner.destination'
        db.delete_column('banners_banner', 'destination')
        
        # Deleting field 'Slot.limit'
        db.delete_column('banners_slot', 'limit')
        
        # Deleting field 'Banner.is_published'
        db.delete_column('banners_banner', 'is_published')
        
        # Deleting field 'Slot.symbol'
        db.delete_column('banners_slot', 'symbol')
        
        # Deleting field 'Slot.rotate'
        db.delete_column('banners_slot', 'rotate')
        
        # Changing field 'Banner.image'
        # (to signature: django.db.models.fields.files.ImageField(max_length=100))
        db.alter_column('banners_banner', 'image', orm['banners.banner:image'])
        
    
    
    models = {
        'banners.banner': {
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'image_rollover': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'popup': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'slot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['banners.Slot']"})
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
