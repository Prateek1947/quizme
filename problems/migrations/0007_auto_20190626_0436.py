# Generated by Django 2.2.2 on 2019-06-26 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0006_auto_20190626_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='statement',
            field=models.TextField(),
        ),
    ]