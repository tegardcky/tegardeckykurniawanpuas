# Generated by Django 4.2.7 on 2023-11-30 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('decky', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_transaksi', models.CharField(max_length=200, null=True)),
                ('nama_depan', models.CharField(max_length=200, null=True)),
                ('nama_belakang', models.CharField(max_length=200, null=True)),
                ('alamat', models.TextField(max_length=200, null=True)),
                ('provinsi', models.CharField(max_length=200, null=True)),
                ('kabupaten', models.CharField(max_length=200, null=True)),
                ('kecamatan', models.CharField(max_length=200, null=True)),
                ('kode_post', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('whatsapp', models.CharField(max_length=200, null=True)),
                ('total_transaksi', models.BigIntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Baru', 'Baru'), ('Lunas', 'Lunas')], default='Baru', max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('tanggal_kirim', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Transaksi',
            },
        ),
        migrations.CreateModel(
            name='DetailTransaksi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_transaksi', models.CharField(max_length=200, null=True)),
                ('jumlah', models.IntegerField(blank=True, null=True)),
                ('produk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='decky.produk')),
            ],
            options={
                'verbose_name_plural': 'Detail Transaksi',
            },
        ),
    ]
