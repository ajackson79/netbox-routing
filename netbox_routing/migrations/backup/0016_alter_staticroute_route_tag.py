# Generated by Django 5.0.9 on 2024-10-22 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_routing', '0015_alter_staticroute_next_hop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticroute',
            name='route_tag',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]