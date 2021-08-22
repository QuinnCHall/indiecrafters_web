# Generated by Django 3.2.4 on 2021-08-22 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membersites', '0004_auto_20210704_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberserver',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=16),
        ),
    ]