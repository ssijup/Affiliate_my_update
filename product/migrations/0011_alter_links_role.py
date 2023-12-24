# Generated by Django 4.2.2 on 2023-12-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_links_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='role',
            field=models.CharField(choices=[('product', 'product'), ('organiser', 'organiser'), ('influencer', 'influencer')], default='product', max_length=50),
        ),
    ]
