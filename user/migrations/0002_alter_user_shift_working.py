# Generated by Django 5.1.2 on 2024-10-19 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='shift_working',
            field=models.CharField(choices=[('A', 'ANNA'), ('B', 'BILLY'), ('C', 'CICI'), ('D', 'DIDI'), ('E', 'EDI')], max_length=20),
        ),
    ]
