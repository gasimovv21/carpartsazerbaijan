# Generated by Django 3.2 on 2023-10-23 22:23

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_parts', '0008_alter_orders_part'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='color',
            field=colorfield.fields.ColorField(default='#0000', help_text='Malin rengin yaz.', image_field=None, max_length=25, samples=None, verbose_name='Malin rengi.'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='part',
            field=models.CharField(choices=[('Spoiler', 'Spoiler'), ('LED işıq', 'LED işıq'), ('Təkər', 'Təkər'), ('Dırnaq', 'Dırnaq'), ('Ayrıqca', 'Ayrıqca'), ('Stop lampa', 'Stop lampa'), ('Aydınlatma', 'Aydınlatma'), ('Motor', 'Motor'), ('Suspension', 'Suspension'), ('Qapı', 'Qapı'), ('Pəncərə', 'Pəncərə'), ('Yan pəncərə', 'Yan pəncərə'), ('Bağaj', 'Bağaj'), ('Stabilizator çubuğu', 'Stabilizator çubuğu'), ('Süspension', 'Süspension'), ('Tormoz', 'Tormoz'), ('Şaquliq', 'Şaquliq'), ('AirBag', 'AirBag'), ('Elektrika', 'Elektrika'), ('İnteriör', 'İnteriör'), ('Təmizlənmə', 'Təmizlənmə'), ('Yağ', 'Yağ'), ('Dəmir', 'Dəmir'), ('Plastik', 'Plastik'), ('Hərəkət', 'Hərəkət'), ('Zincir', 'Zincir'), ('Ağır qışıq', 'Ağır qışıq'), ('Hava filteri', 'Hava filteri'), ('Elektrik sistemi', 'Elektrik sistemi'), ('Dəmir əşyalar', 'Dəmir əşyalar'), ('Süspension parçaları', 'Süspension parçaları'), ('Qapı hissələri', 'Qapı hissələri'), ('Zəngər', 'Zəngər'), ('Difuzor', 'Difuzor'), ('Kuzov', 'Kuzov'), ('Avtomobil yastıqları', 'Avtomobil yastıqları'), ('Təzələmə', 'Təzələmə'), ('Yağ filteri', 'Yağ filteri'), ('Yan qapı', 'Yan qapı'), ('Çubuq', 'Çubuq'), ('Vixlop truba', 'Vixlop truba'), ('İskarpin', 'İskarpin'), ('Labavoy', 'Labavoy'), ('Sirqalar', 'Sirqalar'), ('Vəziyyət', 'Vəziyyət'), ('Qapi elceyi', 'Qapi elceyi')], help_text='Ehtiyat hissesinin kategoriasin seç.', max_length=250, verbose_name='Ehtiyat hissesinin kategoriasi.'),
        ),
    ]