# Generated by Django 2.2.2 on 2019-07-02 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0018_auto_20190702_0853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='solved',
        ),
    ]