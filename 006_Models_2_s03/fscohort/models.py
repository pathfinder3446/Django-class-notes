from django.db import models

class Student(models.Model):
    COUNTRIES = [ # choices = COUNTRIES
        ('TR', 'Turkey'),
        ('US', 'America'),
        ('DE', 'Germany'),
        ('FR', 'France'),
    ]
    first_name = models.CharField('Adı', max_length=50)
    last_name = models.CharField('Soyadı', max_length=50)
    number = models.IntegerField("numara")
    country = models.CharField('Ülke', max_length=2, choices=COUNTRIES, default='TR')
    about = models.TextField('Hakkında', blank=True, null=True)
    avatar = models.ImageField("Resim", upload_to='media/', blank=True, null=True)
    registered_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.number} - {self.first_name}"

    class Meta:
        ordering = ['number']
        verbose_name_plural = 'Öğrenciler'