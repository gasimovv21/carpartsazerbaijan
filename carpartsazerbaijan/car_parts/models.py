from django.db import models


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


class CarBrands(models.Model):
    name = models.TextField(
        verbose_name='Ehtiyat hissesinin mashin markasi',
        help_text='Ehtiyat hissesinin mashin markasin adin yaz.'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ehtiyat hissesinin mashin markasi'
        verbose_name_plural = 'Ehtiyat hisselerin mashin markasi'

    def __str__(self):
        return f'{self.name}'


class Orders(models.Model):
    name = models.TextField(
        verbose_name='Malin adi.',
        help_text='Malin adin yaz.'
    )
    price = models.FloatField(
        verbose_name='Malin sifarish qiymeti.',
        help_text='Malin sifarish qiymetin yaz.'
    )
    price_in_town = models.FloatField(
        verbose_name='Malin Bakidaki qiymeti.',
        help_text='Malin Bakidaki qiymetin yaz. Bilmirsense bosh burax!',
        blank=True,
    )
    cargo_price = models.FloatField(
        verbose_name='Malin kargo qiymeti.',
        help_text='Malin kargo qiymetin yaz.'
    )
    additional_cost = models.TextField(
        verbose_name='Malin elave xercleri.',
        help_text='Malin eger elave xerci olacagsa, misal ucun airbag fln yaza bilersen. Yoxdursa bosh burax!',
        blank=True,
    )
    image = models.ImageField(
        verbose_name='Malin şəkili.',
        help_text='Malin şəkili varsa yukle. Yoxdursa bosh burax!',
        upload_to='car_parts',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Sifarish'
        verbose_name_plural = 'Sifarishler'

    def __str__(self):
        return f'{self.name}'