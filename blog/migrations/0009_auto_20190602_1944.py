# Generated by Django 2.2.1 on 2019-06-02 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_delete_media'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='media',
            new_name='image',
        ),
    ]