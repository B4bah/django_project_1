from django.db import models


class Advertisements(models.Model):
    title = models.CharField(
        verbose_name='Title',
        help_text='Field for products name',
        max_length=100
    )
    description = models.TextField(
        verbose_name='Description'
    )
    price = models.DecimalField(
        verbose_name='Price',
        max_digits=10,
        decimal_places=2,
    )
    auction = models.BooleanField(
        verbose_name='Sale',
        default=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
