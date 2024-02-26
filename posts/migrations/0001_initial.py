# Generated by Django 3.2.4 on 2023-09-06 09:30

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('auto_id', models.PositiveIntegerField(db_index=True, editable=False, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor.fields.RichTextField()),
                ('publication_date', models.DateField()),
                ('image', models.ImageField(upload_to='')),
                ('creator', models.ForeignKey(blank=True, editable=False, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_post_objects', to=settings.AUTH_USER_MODEL)),
                ('updater', models.ForeignKey(blank=True, editable=False, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updater_post_objects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
