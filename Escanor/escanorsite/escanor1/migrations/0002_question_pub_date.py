# Generated by Django 3.0.4 on 2020-04-02 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escanor1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
    ]