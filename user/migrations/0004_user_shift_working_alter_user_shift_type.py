# Generated by Django 5.1.2 on 2024-10-19 10:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_shift_working'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='shift_working',
            field=models.CharField(choices=[('FIX', [('MORNING', 'Morning'), ('MIDDLE', 'Middle'), ('NIGHT', 'Night')]), ('NORMAL', [('ANNA', 'Anna'), ('BILLY', 'Billy'), ('CICI', 'Cici'), ('DIDI', 'Didi'), ('EDI', 'Edi')])], default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='shift_type',
            field=models.CharField(choices=[('FIX', [('MORNING', 'Morning'), ('MIDDLE', 'Middle'), ('NIGHT', 'Night')]), ('NORMAL', [('ANNA', 'Anna'), ('BILLY', 'Billy'), ('CICI', 'Cici'), ('DIDI', 'Didi'), ('EDI', 'Edi')])], default='NORMAL', max_length=20),
        ),
    ]
