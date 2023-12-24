# Generated by Django 4.2.2 on 2023-12-24 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_userrequestingforupgradingtoorganiser_description_and_more'),
        ('product', '0028_refferallink_clicks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.AddField(
            model_name='payment',
            name='refferal_link',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='product.refferallink'),
        ),
        migrations.AddField(
            model_name='payment',
            name='user_details',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='userapp.userdetails'),
        ),
        migrations.AddField(
            model_name='product',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='refferallink',
            name='link_holder_role',
            field=models.CharField(choices=[('influencer', 'influencer'), ('organiser', 'organiser'), ('admin', 'admin')], default='admin', max_length=50),
        ),
    ]
