# Generated by Django 5.1.3 on 2025-05-24 06:52

import django_summernote.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0018_aicategory_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aicategory',
            name='description',
            field=django_summernote.fields.SummernoteTextField(blank=True, null=True),
        ),
    ]
