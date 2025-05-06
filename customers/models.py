from django.db import models

from core.models import BaseModel


class Customer(BaseModel):
    tax_id = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    birth_date = models.DateField()
    info = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "customers"

    
