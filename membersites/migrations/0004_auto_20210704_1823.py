# Generated by Django 3.2.4 on 2021-07-04 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membersites', '0003_auto_20210627_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberserver',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='server/profiles'),
        ),
        migrations.AlterField(
            model_name='memberserver',
            name='server_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='memberserver',
            name='website_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
