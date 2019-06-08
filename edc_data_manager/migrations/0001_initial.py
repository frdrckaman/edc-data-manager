# Generated by Django 2.2.2 on 2019-06-08 23:07

import _socket
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_registration.managers
import edc_sites.models
import edc_utils.date
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edc_registration', '0017_auto_20190305_0123'),
        ('edc_action_item', '0017_auto_20190305_0123'),
        ('edc_visit_schedule', '0003_historicalvisitschedule_visitschedule'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataDictionary',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=250)),
                ('number', models.IntegerField()),
                ('prompt', models.TextField()),
                ('field_name', models.CharField(max_length=250)),
                ('field_type', models.CharField(max_length=250, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Data Dictionary Item',
                'verbose_name_plural': 'Data Dictionary Items',
                'ordering': ('model', 'number', 'prompt'),
            },
        ),
        migrations.CreateModel(
            name='DataManagerUser',
            fields=[
            ],
            options={
                'verbose_name': 'Data Manager User',
                'verbose_name_plural': 'Data Manager Users',
                'proxy': True,
                'default_permissions': ('view',),
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='QuerySubject',
            fields=[
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
                'proxy': True,
                'default_permissions': ('view',),
                'indexes': [],
                'constraints': [],
            },
            bases=('edc_registration.registeredsubject',),
            managers=[
                ('on_site', edc_sites.models.CurrentSiteManager()),
                ('objects', edc_registration.managers.RegisteredSubjectManager()),
            ],
        ),
        migrations.CreateModel(
            name='QueryUser',
            fields=[
            ],
            options={
                'verbose_name': 'Data Query User',
                'verbose_name_plural': 'Data Query Users',
                'proxy': True,
                'default_permissions': ('view',),
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='QueryVisitSchedule',
            fields=[
            ],
            options={
                'verbose_name': 'Visit Schedule',
                'verbose_name_plural': 'Visit Schedule',
                'proxy': True,
                'default_permissions': ('view',),
                'indexes': [],
                'constraints': [],
            },
            bases=('edc_visit_schedule.visitschedule',),
        ),
        migrations.CreateModel(
            name='HistoricalDataQuery',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('action_identifier', models.CharField(db_index=True, max_length=50)),
                ('parent_action_identifier', models.CharField(help_text='action identifier that links to parent reference model instance.', max_length=30, null=True)),
                ('related_action_identifier', models.CharField(help_text='action identifier that links to related reference model instance.', max_length=30, null=True)),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, verbose_name='Query date')),
                ('subject_identifier', models.CharField(editable=False, max_length=50, null=True)),
                ('visit_code_sequence', models.IntegerField(default=0, help_text="Defaults to '0'. For example, when combined with the visit code `1000` would make `1000.0`.", verbose_name='Visit code sequence')),
                ('timepoint', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('query_text', models.TextField(help_text='Describe the query in detail.')),
                ('site_resolved_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Site resolved on')),
                ('site_response_text', models.TextField(blank=True, null=True)),
                ('site_response_status', models.CharField(choices=[('New', 'New'), ('open', 'Open'), ('feedback', 'Feedback'), ('resolved', 'Resolved')], default='New', max_length=25, verbose_name='Site status')),
                ('status', models.CharField(choices=[('open', 'Open'), ('resolved', 'Resolved'), ('resolved_with_action', 'Resolved, with plan of action')], default='open', max_length=25, verbose_name='TCC status')),
                ('resolved_datetime', models.DateTimeField(blank=True, null=True, verbose_name='TCC resolved on')),
                ('plan_of_action', models.TextField(blank=True, help_text='If required, provide a plan of action', null=True)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.ActionItem')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parent_action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.ActionItem')),
                ('recipient', models.ForeignKey(blank=True, db_constraint=False, help_text='select a name from the list', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_data_manager.QueryUser', verbose_name='Sent to')),
                ('registered_subject', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_data_manager.QuerySubject', verbose_name='Subject Identifier')),
                ('related_action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.ActionItem')),
                ('resolved_user', models.ForeignKey(blank=True, db_constraint=False, help_text='select a name from the list', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_data_manager.DataManagerUser', verbose_name='TCC resolved by')),
                ('sender', models.ForeignKey(blank=True, db_constraint=False, help_text='select a name from the list', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_data_manager.DataManagerUser', verbose_name='Query raised by')),
                ('visit_schedule', models.ForeignKey(blank=True, db_constraint=False, help_text='select all that apply', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_data_manager.QueryVisitSchedule', verbose_name='Visit')),
            ],
            options={
                'verbose_name': 'historical Data Query',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDataDictionary',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('model', models.CharField(max_length=250)),
                ('number', models.IntegerField()),
                ('prompt', models.TextField()),
                ('field_name', models.CharField(max_length=250)),
                ('field_type', models.CharField(max_length=250, null=True)),
                ('active', models.BooleanField(default=False)),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Data Dictionary Item',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='DataQuery',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('action_identifier', models.CharField(max_length=50, unique=True)),
                ('parent_action_identifier', models.CharField(help_text='action identifier that links to parent reference model instance.', max_length=30, null=True)),
                ('related_action_identifier', models.CharField(help_text='action identifier that links to related reference model instance.', max_length=30, null=True)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, verbose_name='Query date')),
                ('subject_identifier', models.CharField(editable=False, max_length=50, null=True)),
                ('visit_code_sequence', models.IntegerField(default=0, help_text="Defaults to '0'. For example, when combined with the visit code `1000` would make `1000.0`.", verbose_name='Visit code sequence')),
                ('timepoint', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('query_text', models.TextField(help_text='Describe the query in detail.')),
                ('site_resolved_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Site resolved on')),
                ('site_response_text', models.TextField(blank=True, null=True)),
                ('site_response_status', models.CharField(choices=[('New', 'New'), ('open', 'Open'), ('feedback', 'Feedback'), ('resolved', 'Resolved')], default='New', max_length=25, verbose_name='Site status')),
                ('status', models.CharField(choices=[('open', 'Open'), ('resolved', 'Resolved'), ('resolved_with_action', 'Resolved, with plan of action')], default='open', max_length=25, verbose_name='TCC status')),
                ('resolved_datetime', models.DateTimeField(blank=True, null=True, verbose_name='TCC resolved on')),
                ('plan_of_action', models.TextField(blank=True, help_text='If required, provide a plan of action', null=True)),
                ('action_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='edc_action_item.ActionItem')),
                ('data_dictionaries', models.ManyToManyField(blank=True, help_text='select all that apply', to='edc_data_manager.DataDictionary', verbose_name='Question(s)')),
                ('parent_action_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='edc_action_item.ActionItem')),
                ('recipient', models.ForeignKey(help_text='select a name from the list', on_delete=django.db.models.deletion.PROTECT, related_name='recipient', to='edc_data_manager.QueryUser', verbose_name='Sent to')),
                ('registered_subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='edc_data_manager.QuerySubject', verbose_name='Subject Identifier')),
                ('related_action_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='edc_action_item.ActionItem')),
                ('resolved_user', models.ForeignKey(blank=True, help_text='select a name from the list', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='resolved_user', to='edc_data_manager.DataManagerUser', verbose_name='TCC resolved by')),
                ('sender', models.ForeignKey(help_text='select a name from the list', on_delete=django.db.models.deletion.PROTECT, related_name='sender', to='edc_data_manager.DataManagerUser', verbose_name='Query raised by')),
                ('visit_schedule', models.ForeignKey(blank=True, help_text='select all that apply', null=True, on_delete=django.db.models.deletion.PROTECT, to='edc_data_manager.QueryVisitSchedule', verbose_name='Visit')),
            ],
            options={
                'verbose_name': 'Data Query',
                'verbose_name_plural': 'Data Queries',
            },
        ),
    ]
