# Generated by Django 5.0.3 on 2024-03-25 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stdapp', '0004_rename_age_person_page_rename_date_person_pdate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='pdate',
            new_name='date',
        ),
    ]