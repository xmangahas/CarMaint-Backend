# Generated by Django 2.2.7 on 2019-11-14 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carmaint', '0003_auto_20191114_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenance',
            name='labor_cost',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='oil_change',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='parts_cost',
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='invoice_img',
            field=models.CharField(blank=True, default='', max_length=600),
        ),
    ]