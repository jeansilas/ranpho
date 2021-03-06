# Generated by Django 3.2.8 on 2021-11-04 20:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0004_auto_20211104_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='pic',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='album.album'),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
