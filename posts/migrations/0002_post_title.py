# Generated by Django 4.1.3 on 2022-11-13 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='DEFAULT_VALUE', max_length=255),
            preserve_default=False,
        ),
    ]