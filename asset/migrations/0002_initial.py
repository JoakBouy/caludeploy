# Generated by Django 3.2.16 on 2023-08-12 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asset', '0001_initial'),
        ('community', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.event'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.community'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='announcement_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='announcement',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='announcement_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='albumimage',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.album'),
        ),
        migrations.AddField(
            model_name='albumimage',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='album_image_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='album',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_created_in', to='community.community'),
        ),
        migrations.AddField(
            model_name='album',
            name='community_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='album_linked_to', to='community.communityevent'),
        ),
        migrations.AddField(
            model_name='album',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='album_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='album',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='album_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
