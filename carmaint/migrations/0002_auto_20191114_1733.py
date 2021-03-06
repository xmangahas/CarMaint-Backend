# Generated by Django 2.2.7 on 2019-11-14 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carmaint', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maintenance',
            old_name='cycle_mileage',
            new_name='mileage',
        ),
        migrations.RemoveField(
            model_name='car',
            name='vin',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='due_mileage',
        ),
        migrations.AddField(
            model_name='car',
            name='image_url',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AddField(
            model_name='car',
            name='trim',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='cost',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=8),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='invoice_img',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='oil_change',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='desc',
            field=models.CharField(default='', max_length=500),
        ),
    ]
