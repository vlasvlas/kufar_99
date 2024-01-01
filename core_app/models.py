from django.db import models


class Notebook(models.Model):
    """ Ноутбуки """

    url = models.CharField(max_length=255, unique=True, verbose_name='Ссылка')
    title = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    manufacturer = models.CharField(max_length=200)
    diagonal = models.CharField(max_length=50)
    screen_resolution = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    processor = models.CharField(max_length=100)
    op_mem = models.CharField(max_length=100)
    type_video_card = models.CharField(max_length=50)
    video_card = models.CharField(max_length=100)
    type_drive = models.CharField(max_length=50)
    capacity_drive = models.CharField(max_length=100)
    auto_work_time = models.CharField(max_length=20)
    state = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'

    def __str__(self):
        return f'{self.title} | {self.price}'


class Images(models.Model):
    """ Изображения """

    image = models.URLField(max_length=255, unique=True)
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, related_name='image')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.image



