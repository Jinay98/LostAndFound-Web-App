# Generated by Django 2.0.7 on 2018-10-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180912_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.IntegerField(default=0)),
                ('Description', models.CharField(default='', max_length=150)),
                ('Location', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
