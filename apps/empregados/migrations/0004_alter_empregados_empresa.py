# Generated by Django 4.0.3 on 2022-05-09 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('empregados', '0003_alter_empregados_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empregados',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
        ),
    ]
