# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Document'
        db.create_table(u'project_document', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('doc', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add='true', blank=True)),
        ))
        db.send_create_signal(u'project', ['Document'])

        # Adding model 'Club'
        db.create_table(u'project_club', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2500)),
        ))
        db.send_create_signal(u'project', ['Club'])

        # Adding M2M table for field cores on 'Club'
        m2m_table_name = db.shorten_name(u'project_club_cores')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('club', models.ForeignKey(orm[u'project.club'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['club_id', 'user_id'])

        # Adding model 'Project'
        db.create_table(u'project_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(related_name='parent_club', to=orm['project.Club'])),
            ('brief', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('budget', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal(u'project', ['Project'])

        # Adding M2M table for field users on 'Project'
        m2m_table_name = db.shorten_name(u'project_project_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'project.project'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'user_id'])

        # Adding M2M table for field mentors on 'Project'
        m2m_table_name = db.shorten_name(u'project_project_mentors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'project.project'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'user_id'])

        # Adding M2M table for field documents on 'Project'
        m2m_table_name = db.shorten_name(u'project_project_documents')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'project.project'], null=False)),
            ('document', models.ForeignKey(orm[u'project.document'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'document_id'])

        # Adding model 'Comment'
        db.create_table(u'project_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add='true', blank=True)),
        ))
        db.send_create_signal(u'project', ['Comment'])

        # Adding model 'Update'
        db.create_table(u'project_update', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='update_creator', to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=2500)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add='true', blank=True)),
        ))
        db.send_create_signal(u'project', ['Update'])

        # Adding M2M table for field comments on 'Update'
        m2m_table_name = db.shorten_name(u'project_update_comments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('update', models.ForeignKey(orm[u'project.update'], null=False)),
            ('comment', models.ForeignKey(orm[u'project.comment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['update_id', 'comment_id'])

        # Adding model 'Task'
        db.create_table(u'project_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='task_creator', to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=2500)),
            ('deadline', self.gf('django.db.models.fields.DateTimeField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add='true', blank=True)),
            ('percent', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'project', ['Task'])

        # Adding M2M table for field assigned on 'Task'
        m2m_table_name = db.shorten_name(u'project_task_assigned')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('task', models.ForeignKey(orm[u'project.task'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['task_id', 'user_id'])

        # Adding M2M table for field comments on 'Task'
        m2m_table_name = db.shorten_name(u'project_task_comments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('task', models.ForeignKey(orm[u'project.task'], null=False)),
            ('comment', models.ForeignKey(orm[u'project.comment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['task_id', 'comment_id'])


    def backwards(self, orm):
        # Deleting model 'Document'
        db.delete_table(u'project_document')

        # Deleting model 'Club'
        db.delete_table(u'project_club')

        # Removing M2M table for field cores on 'Club'
        db.delete_table(db.shorten_name(u'project_club_cores'))

        # Deleting model 'Project'
        db.delete_table(u'project_project')

        # Removing M2M table for field users on 'Project'
        db.delete_table(db.shorten_name(u'project_project_users'))

        # Removing M2M table for field mentors on 'Project'
        db.delete_table(db.shorten_name(u'project_project_mentors'))

        # Removing M2M table for field documents on 'Project'
        db.delete_table(db.shorten_name(u'project_project_documents'))

        # Deleting model 'Comment'
        db.delete_table(u'project_comment')

        # Deleting model 'Update'
        db.delete_table(u'project_update')

        # Removing M2M table for field comments on 'Update'
        db.delete_table(db.shorten_name(u'project_update_comments'))

        # Deleting model 'Task'
        db.delete_table(u'project_task')

        # Removing M2M table for field assigned on 'Task'
        db.delete_table(db.shorten_name(u'project_task_assigned'))

        # Removing M2M table for field comments on 'Task'
        db.delete_table(db.shorten_name(u'project_task_comments'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'project.club': {
            'Meta': {'object_name': 'Club'},
            'cores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'project.comment': {
            'Meta': {'object_name': 'Comment'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': "'true'", 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'project.document': {
            'Meta': {'object_name': 'Document'},
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'doc': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': "'true'", 'blank': 'True'})
        },
        u'project.project': {
            'Meta': {'object_name': 'Project'},
            'brief': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'budget': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parent_club'", 'to': u"orm['project.Club']"}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'documents': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['project.Document']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mentors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'project_mentor'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'project_member'", 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        },
        u'project.task': {
            'Meta': {'object_name': 'Task'},
            'assigned': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'task_assigned'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['project.Comment']", 'symmetrical': 'False'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '2500'}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"}),
            'percent': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': "'true'", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'task_creator'", 'to': u"orm['auth.User']"})
        },
        u'project.update': {
            'Meta': {'object_name': 'Update'},
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['project.Comment']", 'symmetrical': 'False'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '2500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': "'true'", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'update_creator'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['project']