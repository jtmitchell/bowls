# Generated by Django 3.2.3 on 2021-06-01 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('teams', models.ManyToManyField(to='clubs.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Draw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('draw_type', models.CharField(choices=[('roundrobin', 'Round Robin'), ('knockout', 'Knockout Round')], db_index=True, default='roundrobin', max_length=20)),
                ('draw_order', models.IntegerField(default=1)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.competition')),
                ('teams', models.ManyToManyField(to='clubs.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('draw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.draw')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.game')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.team')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.location'),
        ),
        migrations.AddField(
            model_name='game',
            name='teams',
            field=models.ManyToManyField(to='clubs.Team'),
        ),
    ]
