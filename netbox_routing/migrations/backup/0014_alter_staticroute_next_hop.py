# Generated by Django 5.0.9 on 2024-10-22 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_routing', '0013_staticroute_route_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticroute',
            name='next_hop',
            field=models.GenericIPAddressField(),
        ),
    ]
