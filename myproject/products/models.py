from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    summary = models.TextField(default="This is cool!")
    valid = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('product:delete_product', kwargs={"product_id": self.id})

    def get_absolute_url_for_edit(self):
        return reverse('product:edit_product', kwargs={"product_id": self.id})
