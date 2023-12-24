# Generated by Django 4.2.2 on 2023-12-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_product_product_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refferallink',
            name='link_holder_role',
            field=models.CharField(choices=[('influencer', 'influencer'), ('organiser', 'organiser'), ('admin', 'admin')], default='admin', max_length=50),
        ),
    ]
