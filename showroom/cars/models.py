from django.db import models


class cars_data(models.Model):
    name = models.CharField(max_length=100)
    model = models.IntegerField()
    maker = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    registration_no = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Cars Data'


