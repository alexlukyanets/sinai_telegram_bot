# Generated by Django 4.2.7 on 2023-12-01 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0004_rename_menu_text_id_menulevel_level_text_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='text_reply',
            field=models.TextField(blank=True, null=True),
        ),
    ]
