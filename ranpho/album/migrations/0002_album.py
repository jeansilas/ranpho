# Generated by Django 3.2.8 on 2021-11-04 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='album.pic')),
            ],
        ),
    ]
