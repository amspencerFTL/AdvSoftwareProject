# Generated by Django 5.0.3 on 2024-04-27 21:25

import django.core.validators
import storages.backends.s3
import whistleblower.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whistleblower', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='evidence',
            field=models.FileField(blank=True, null=True, storage=storages.backends.s3.S3Storage(), upload_to=whistleblower.models.create_new_file_name, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'txt', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='report',
            name='file',
            field=models.FileField(blank=True, null=True, storage=storages.backends.s3.S3Storage(), upload_to=whistleblower.models.create_new_file_name, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'txt', 'jpg', 'jpeg'])]),
        ),
    ]
