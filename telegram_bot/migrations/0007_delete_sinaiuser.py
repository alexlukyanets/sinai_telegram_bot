# Generated by Django 4.2.7 on 2023-12-06 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0006_menuitem_menu_reply'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SinaiUser',
        ),
    ]