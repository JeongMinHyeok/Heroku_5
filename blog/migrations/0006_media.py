# Generated by Django 2.2.1 on 2019-06-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190531_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]
