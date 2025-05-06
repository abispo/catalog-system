# from django.db import models


# class Customer(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=200)
#     tax_id = models.CharField(max_length=11, unique=True, verbose_name="CPF")
#     birth_date = models.DateField()
#     email = models.CharField(max_length=200)
#     entry_date = models.DateTimeField(auto_now_add=True)
#     info = models.CharField(max_length=1000, blank=True, null=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

#     class Meta:
#         db_table = "customers"

    
