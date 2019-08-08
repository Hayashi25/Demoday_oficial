# Generated by Django 2.2.4 on 2019-08-04 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20190804_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escola',
            name='email_escola',
        ),
        migrations.AddField(
            model_name='escola',
            name='email',
            field=models.EmailField(default=1, max_length=255, unique=True, verbose_name='Email da Escola'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='escola',
            name='codigo_acesso',
            field=models.CharField(max_length=12, unique=True, verbose_name='Registre o código de acesso'),
        ),
        migrations.AlterField(
            model_name='escola',
            name='endereco_escola',
            field=models.CharField(max_length=255, unique=True, verbose_name='Endereço da Escola'),
        ),
        migrations.AlterField(
            model_name='escola',
            name='nome_escola',
            field=models.CharField(max_length=255, unique=True, verbose_name='Nome da Escola'),
        ),
        migrations.AlterField(
            model_name='escola',
            name='senha_acesso',
            field=models.CharField(max_length=12, unique=True, verbose_name='Registre a senha de acesso'),
        ),
        migrations.AlterField(
            model_name='escola',
            name='telefone_escola',
            field=models.CharField(max_length=12, unique=True, verbose_name='Telefone da Escola'),
        ),
    ]
