from django.db import models
from colorfield.fields import ColorField
from django.conf import settings


class CarParts(models.Model):
    name = models.TextField(
        verbose_name='Ehtiyat hissesinin adi.',
        help_text='Ehtiyat hissesinin adin yaz.'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ehtiyat hissesi'
        verbose_name_plural = 'Ehtiyat hisseleri'

    def __str__(self):
        return f'{self.name}'


class Orders(models.Model):
    name = models.TextField(
        verbose_name='Malin adi.',
        help_text='Malin adin yaz.'
    )
    part = models.CharField(
        max_length=250,
        verbose_name='Ehtiyat hissesinin kategoriasi.',
        help_text='Ehtiyat hissesinin kategoriasin seç.',
        choices=settings.CAR_PARTS_CHOICES
    )
    brand = models.CharField(
        max_length=50,
        verbose_name='Ehtiyat hissesinin mashin markasin kategoriasi.',
        help_text='Ehtiyat hissesinin mashin markasinin kategoriasin seç.',
        choices=settings.CAR_BRANDS_CHOICES
    )
    price = models.FloatField(
        verbose_name='Malin sifarish qiymeti.',
        help_text='Malin sifarish qiymetin yaz.'
    )
    price_in_town = models.FloatField(
        verbose_name='Malin Bakidaki qiymeti.',
        help_text='Malin Bakidaki qiymetin yaz. Bilmirsense bosh burax!',
        blank=True
    )
    cargo_price = models.FloatField(
        verbose_name='Malin kargo qiymeti.',
        help_text='Malin kargo qiymetin yaz.'
    )
    additional_cost = models.TextField(
        verbose_name='Malin elave xercleri.',
        help_text='Malin eger elave xerci olacagsa, misal ucun airbag fln yaza bilersen. Yoxdursa bosh burax!',
        blank=True
    )
    image = models.ImageField(
        verbose_name='Malin şəkili.',
        help_text='Malin şəkili varsa yukle. Yoxdursa bosh burax!',
        upload_to='car_parts'
    )
    color = ColorField(
        default='#0000',
        verbose_name='Malin rengi.',
        help_text='Malin rengin sec.'
        )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Sifarish'
        verbose_name_plural = 'Sifarishler'

    def __str__(self):
        return f'{self.name}'