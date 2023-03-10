# Generated by Django 4.1.6 on 2023-02-09 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=20)),
                ('email', models.CharField(default='', max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.BigIntegerField()),
                ('gender', models.CharField(max_length=15)),
                ('username', models.IntegerField()),
                ('password', models.CharField(default='', max_length=20)),
                ('company_name', models.CharField(max_length=30)),
                ('holder_name', models.CharField(max_length=20)),
                ('ifsc', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('account_number', models.BigIntegerField()),
                ('image', models.ImageField(default='', upload_to='seller/')),
                ('status', models.CharField(default='pending', max_length=20)),
            ],
            options={
                'db_table': 'seller',
            },
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
