# Generated by Django 5.1.6 on 2025-04-01 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0003_alter_userprofile_role'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_add_book', 'Can add a book'), ('can_change_book', 'Can change a book'), ('can_delete_book', 'Can delete a book')]},
        ),
    ]
