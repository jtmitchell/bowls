# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Club'
        db.create_table(u'clubs_club', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('contact', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
        ))
        db.send_create_signal(u'clubs', ['Club'])

        # Adding model 'Team'
        db.create_table(u'clubs_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'clubs', ['Team'])

        # Adding model 'Player'
        db.create_table(u'clubs_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('given_name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('family_name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clubs.Club'], null=True, blank=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clubs.Team'])),
        ))
        db.send_create_signal(u'clubs', ['Player'])


    def backwards(self, orm):
        # Deleting model 'Club'
        db.delete_table(u'clubs_club')

        # Deleting model 'Team'
        db.delete_table(u'clubs_team')

        # Deleting model 'Player'
        db.delete_table(u'clubs_player')


    models = {
        u'clubs.club': {
            'Meta': {'object_name': 'Club'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'contact': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'clubs.player': {
            'Meta': {'object_name': 'Player'},
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clubs.Club']", 'null': 'True', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clubs.Team']"})
        },
        u'clubs.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['clubs']