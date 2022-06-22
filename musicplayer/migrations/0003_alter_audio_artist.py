# Generated by Django 4.0.5 on 2022-06-22 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicplayer', '0002_rename_first_name_musician_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audio', to='musicplayer.musician'),
        ),
    ]
