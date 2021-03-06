# Generated by Django 2.1.2 on 2018-10-16 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respondent', models.CharField(max_length=15, null=True)),
                ('date', models.DateTimeField(verbose_name='response date')),
            ],
        ),
        migrations.CreateModel(
            name='Targets',
            fields=[
                ('index_key', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='response',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a.Targets'),
        ),
    ]
