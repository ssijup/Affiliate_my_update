# Generated by Django 4.2.2 on 2023-12-22 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0011_alter_links_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='RefferalLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('link_holder_role', models.CharField(choices=[('product', 'product'), ('influencer', 'influencer'), ('organiser', 'organiser')], default='product', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('direct_referred_link_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direct_referred_links', to=settings.AUTH_USER_MODEL)),
                ('indirect_referred_link_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indirect_referred_links', to=settings.AUTH_USER_MODEL)),
                ('link_generated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_generator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='unique_id',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='Links',
        ),
        migrations.AddField(
            model_name='refferallink',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
