# Generated by Django 5.1.7 on 2025-05-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_remove_member_firstname_remove_member_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
