# Generated by Django 3.2 on 2023-10-23 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_parts', '0006_orders_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='brand',
            field=models.CharField(choices=[('Toyota', 'Toyota'), ('Ford', 'Ford'), ('Honda', 'Honda'), ('Chevrolet', 'Chevrolet'), ('Nissan', 'Nissan'), ('Volkswagen', 'Volkswagen'), ('BMW', 'BMW'), ('Mercedes-Benz', 'Mercedes-Benz'), ('Audi', 'Audi'), ('Hyundai', 'Hyundai'), ('Kia', 'Kia'), ('Mazda', 'Mazda'), ('Subaru', 'Subaru'), ('Jeep', 'Jeep'), ('Lexus', 'Lexus'), ('Chrysler', 'Chrysler'), ('Volvo', 'Volvo'), ('Porsche', 'Porsche'), ('Jaguar', 'Jaguar'), ('Land Rover', 'Land Rover')], default=None, help_text='Ehtiyat hissesinin mashin markasinin kategoriasin seç.', max_length=50, verbose_name='Ehtiyat hissesinin mashin markasin kategoriasi.'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CarBrands',
        ),
    ]