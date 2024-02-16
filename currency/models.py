from django.db import models


class Currency(models.Model):
    name = models.CharField('Наименование валюты', max_length=64)
    charcode = models.CharField('Код валюты', max_length=3)
    date = models.DateField('Дата курса')
    rate = models.FloatField('Курс')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['charcode', 'date'],
                name='unique_date_charcode'
            )
        ]
        ordering = ('name',)
