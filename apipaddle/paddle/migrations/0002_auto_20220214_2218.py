# Generated by Django 3.2.9 on 2022-02-14 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paddle', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='price',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='product',
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paddle.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paddle.sale')),
            ],
        ),
    ]