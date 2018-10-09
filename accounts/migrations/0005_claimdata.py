# Generated by Django 2.0.7 on 2018-10-09 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_requestdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaimData',
            fields=[
                ('ClaimID', models.AutoField(primary_key=True, serialize=False)),
                ('Location', models.CharField(default='', max_length=100)),
                ('ItemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ItemData')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
