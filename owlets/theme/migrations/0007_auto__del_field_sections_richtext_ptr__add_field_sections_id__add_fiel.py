# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Sections.richtext_ptr'
        db.delete_column(u'theme_sections', u'richtext_ptr_id')

        # Adding field 'Sections.id'
        db.add_column(u'theme_sections', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)

        # Adding field 'Sections._order'
        db.add_column(u'theme_sections', '_order',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


        # Changing field 'Sections.content'
        db.alter_column(u'theme_sections', 'content', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Adding field 'Sections.richtext_ptr'
        db.add_column(u'theme_sections', u'richtext_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['theme.RichText'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'Sections.id'
        db.delete_column(u'theme_sections', u'id')

        # Deleting field 'Sections._order'
        db.delete_column(u'theme_sections', '_order')


        # Changing field 'Sections.content'
        db.alter_column(u'theme_sections', 'content', self.gf('mezzanine.core.fields.RichTextField')())

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
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'theme.fees': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Fees'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'fees_age': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fees_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fees_link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fees_price': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
            'what_we_do_heading': ('django.db.models.fields.CharField', [], {'default': "'some of the things we get upto'", 'max_length': '200'}),
            'what_we_do_link': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'theme.parentssaying': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'ParentsSaying'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parentssaying'", 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'saying_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'saying_quote': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'theme.richtext': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'RichText', '_ormbases': [u'pages.Page']},
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True'}),
            'intropara': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'theme.sections': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Sections'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'section'", 'to': u"orm['theme.RichText']"})
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