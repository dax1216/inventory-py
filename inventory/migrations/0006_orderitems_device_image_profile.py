# Generated by Django 4.2 on 2023-05-21 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0005_alter_orderitems_options_alter_ordernotes_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='device_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default.jpg', upload_to='profile_images')),
                ('department', models.CharField(choices=[('PBB', 'PBB'), ('ADMIN_HR', 'Admin/HR'), ('FINANCE', 'Finance'), ('ELP', 'ELP')], default='PBB', max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
