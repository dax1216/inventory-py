# Generated by Django 4.2 on 2023-05-24 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_orderitems_device_image_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='device_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]