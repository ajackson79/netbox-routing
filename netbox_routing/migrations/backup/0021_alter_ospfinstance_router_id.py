# Generated by Django 5.0.9 on 2024-10-27 13:24

import netbox_routing.fields.ip
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_routing', '0020_alter_ospfinstance_router_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ospfinstance',
            name='router_id',
            field=netbox_routing.fields.ip.IPAddressField(),
        ),
    ]
