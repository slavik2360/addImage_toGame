# Generated by Django 4.2.3 on 2023-07-23 07:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_rename_imgor_game_main_imgor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitecard',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 22, 13, 54, 14, 232909), verbose_name='дата истечения'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='games/unknown.png', upload_to='games/', verbose_name='изображение')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='games.game')),
            ],
        ),
    ]
