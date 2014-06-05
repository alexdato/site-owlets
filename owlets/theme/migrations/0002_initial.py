# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HomePage'
        db.create_table(u'theme_homepage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('introduction_heading', self.gf('django.db.models.fields.CharField')(default='start a love for learning', max_length=200)),
            ('arrange_visit_link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('see_our_setting_link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('welcome_heading', self.gf('django.db.models.fields.CharField')(default='welcome to owlets', max_length=200)),
            ('welcome_text', self.gf('django.db.models.fields.TextField')()),
            ('welcome_link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('what_we_do_heading', self.gf('django.db.models.fields.CharField')(default='some of the things we get upto', max_length=200)),
            ('what_people_are_saying_heading', self.gf('django.db.models.fields.CharField')(default='what parents are saying', max_length='200')),
            ('our_fees_heading', self.gf('django.db.models.fields.CharField')(default='our fees', max_length='200')),
        ))
        db.send_create_signal(u'theme', ['HomePage'])

        # Adding model 'Slide'
        db.create_table(u'theme_slide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='slides', to=orm['theme.HomePage'])),
            ('image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'theme', ['Slide'])

        # Adding model 'DoBox'
        db.create_table(u'theme_dobox', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dobox', to=orm['theme.HomePage'])),
            ('image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True)),
        ))
        db.send_create_signal(u'theme', ['DoBox'])

        # Adding model 'ParentsSaying'
        db.create_table(u'theme_parentssaying', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='parentssaying', to=orm['theme.HomePage'])),
            ('saying_quote', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('saying_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'theme', ['ParentsSaying'])

        # Adding model 'Fees'
        db.create_table(u'theme_fees', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fees', to=orm['theme.HomePage'])),
            ('fees_age', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fees_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fees_link', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'theme', ['Fees'])


    def backwards(self, orm):
        # Deleting model 'HomePage'
        db.delete_table(u'theme_homepage')

        # Deleting model 'Slide'
        db.delete_table(u'theme_slide')

        # Deleting model 'DoBox'
        db.delete_table(u'theme_dobox')

        # Deleting model 'ParentsSaying'
        db.delete_table(u'theme_parentssaying')

        # Deleting model 'Fees'
        db.delete_table(u'theme_fees')


    models = {
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'theme.dobox': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'DoBox'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dobox'", 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True'})
        },
        u'theme.fees': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Fees'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'fees_age': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fees_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fees_link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fees'", 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'theme.homepage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'HomePage', '_ormbases': [u'pages.Page']},
            'arrange_visit_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'introduction_heading': ('django.db.models.fields.CharField', [], {'default': "'start a love for learning'", 'max_length': '200'}),
            'our_fees_heading': ('django.db.models.fields.CharField', [], {'default': "'our fees'", 'max_length': "'200'"}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'see_our_setting_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'welcome_heading': ('django.db.models.fields.CharField', [], {'default': "'welcome to owlets'", 'max_length': '200'}),
            'welcome_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'welcome_text': ('django.db.models.fields.TextField', [], {}),
            'what_people_are_saying_heading': ('django.db.models.fields.CharField', [], {'default': "'what parents are saying'", 'max_length': "'200'"}),
            'what_we_do_heading': ('django.db.models.fields.CharField', [], {'default': "'some of the things we get upto'", 'max_length': '200'})
        },
        u'theme.parentssaying': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'ParentsSaying'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parentssaying'", 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'saying_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'saying_quote': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'theme.slide': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Slide'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slides'", 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['theme']