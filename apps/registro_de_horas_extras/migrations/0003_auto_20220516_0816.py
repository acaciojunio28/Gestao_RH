# Generated by Django 3.1.6 on 2022-05-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_de_horas_extras', '0002_registrohoras_empregados'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoras',
            name='horas',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registrohoras',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]