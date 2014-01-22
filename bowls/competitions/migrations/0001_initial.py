# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'competitions_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'competitions', ['Location'])

        # Adding model 'Competition'
        db.create_table(u'competitions_competition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
        ))
        db.send_create_signal(u'competitions', ['Competition'])

        # Adding M2M table for field teams on 'Competition'
        db.create_table(u'competitions_competition_teams', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('competition', models.ForeignKey(orm[u'competitions.competition'], null=False)),
            ('team', models.ForeignKey(orm[u'clubs.team'], null=False))
        ))
        db.create_unique(u'competitions_competition_teams', ['competition_id', 'team_id'])

        # Adding model 'Draw'
        db.create_table(u'competitions_draw', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('competition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['competitions.Competition'])),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('draw_type', self.gf('django.db.models.fields.CharField')(default='roundrobin', max_length=20, db_index=True)),
            ('draw_order', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'competitions', ['Draw'])

        # Adding M2M table for field teams on 'Draw'
        db.create_table(u'competitions_draw_teams', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('draw', models.ForeignKey(orm[u'competitions.draw'], null=False)),
            ('team', models.ForeignKey(orm[u'clubs.team'], null=False))
        ))
        db.create_unique(u'competitions_draw_teams', ['draw_id', 'team_id'])

        # Adding model 'Game'
        db.create_table(u'competitions_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('draw', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['competitions.Draw'])),
            ('start_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['competitions.Location'])),
        ))
        db.send_create_signal(u'competitions', ['Game'])

        # Adding M2M table for field teams on 'Game'
        db.create_table(u'competitions_game_teams', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm[u'competitions.game'], null=False)),
            ('team', models.ForeignKey(orm[u'clubs.team'], null=False))
        ))
        db.create_unique(u'competitions_game_teams', ['game_id', 'team_id'])

        # Adding model 'Result'
        db.create_table(u'competitions_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['competitions.Game'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clubs.Team'])),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'competitions', ['Result'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'competitions_location')

        # Deleting model 'Competition'
        db.delete_table(u'competitions_competition')

        # Removing M2M table for field teams on 'Competition'
        db.delete_table('competitions_competition_teams')

        # Deleting model 'Draw'
        db.delete_table(u'competitions_draw')

        # Removing M2M table for field teams on 'Draw'
        db.delete_table('competitions_draw_teams')

        # Deleting model 'Game'
        db.delete_table(u'competitions_game')

        # Removing M2M table for field teams on 'Game'
        db.delete_table('competitions_game_teams')

        # Deleting model 'Result'
        db.delete_table(u'competitions_result')


    models = {
        u'clubs.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'competitions.competition': {
            'Meta': {'object_name': 'Competition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['clubs.Team']", 'symmetrical': 'False'})
        },
        u'competitions.draw': {
            'Meta': {'object_name': 'Draw'},
            'competition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['competitions.Competition']"}),
            'draw_order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'draw_type': ('django.db.models.fields.CharField', [], {'default': "'roundrobin'", 'max_length': '20', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['clubs.Team']", 'symmetrical': 'False'})
        },
        u'competitions.game': {
            'Meta': {'object_name': 'Game'},
            'draw': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['competitions.Draw']"}),
            'end_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['competitions.Location']"}),
            'start_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['clubs.Team']", 'symmetrical': 'False'})
        },
        u'competitions.location': {
            'Meta': {'object_name': 'Location'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'competitions.result': {
            'Meta': {'object_name': 'Result'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['competitions.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clubs.Team']"})
        }
    }

    complete_apps = ['competitions']