"""
Django migration file for updating the Task model in the tasks app.

This migration removes the `completed` field, adds a new
`status` field, and updates the database schema accordingly.
"""
from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Migration for updating the Task model in the tasks app.
    This class removes fields and adds new fields to match the updated schema.
    """

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('not_started',
            'Not yet started'), ('in_progress', 'In progress'),
            ('completed', 'Completed')],
            default='not_started', max_length=20),
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(),
        ),
    ]
