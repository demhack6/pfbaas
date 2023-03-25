# Generated by Django 4.1.7 on 2023-03-25 17:50

import browserbox.models
import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('browserbox', '0003_browser_box_without_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryBrowserBox',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ip', models.GenericIPAddressField()),
                ('create_dt', models.DateTimeField(default=datetime.datetime.now)),
                ('terminate_dt', models.DateTimeField(default=browserbox.models._add_30_minutes)),
            ],
            options={
                'verbose_name': 'history_browser_box',
                'verbose_name_plural': 'history_browser_boxes',
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='BrowserBoxSession',
        ),
    ]
