# Generated by Django 5.0.9 on 2024-10-27 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_routing', '0017_alter_ospfinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ospfinstance',
            options={'ordering': ('router_id', 'name', 'device', 'vrf')},
        ),
    ]
