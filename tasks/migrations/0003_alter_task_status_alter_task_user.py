"""
Django migration for altering Task model fields.

This migration modifies the Task model fields `status` and `user`
to fit new schema requirements.
"""

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Migration to alter Task model fields `status` and `user`.
    """

    dependencies = [
        ('tasks',
        '0002_remove_task_completed_task_status_task_updated_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('not_started',
            'Not Started'), ('in_progress', 'In Progress'),
            ('completed', 'Completed')],
            default='not_started',
            max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='tasks',
                to=settings.AUTH_USER_MODEL),
        ),
    ]
