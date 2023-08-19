from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()


class Advertisement(models.Model):
    image = models.ImageField(
        verbose_name='Image',
        upload_to='advertisements/'
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='User'
    )

    title = models.CharField(
        verbose_name='Title',
        help_text='Field for product name',
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

    @admin.display(description='Creation date')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Today at {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y at %H:%M:%S")

    @admin.display(description='Last updated')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.strftime('%H:%M:%S')
            return format_html(
                '<span style="color: red; font-weight: bold;">Today at {}</span>', updated_time
            )
        return self.updated_at.strftime("%d.%m.%Y at %H:%M:%S")

    @admin.display(description='Show image')
    def Show_image(self):
        if self.image:
            return format_html('<img scr={} style="width: 50px; height: 50px">', self.image.url)

    def __str__(self):
        return f'<id={self.id} title={self.title} price={self.price:.2f}>'

    class Meta:
        db_table = 'advertisement'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
