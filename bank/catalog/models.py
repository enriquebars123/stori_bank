from django.db import models

# Create your models here.

class Transaction(models.Model):
    account_number = models.CharField(max_length=50,blank=False, null = False, verbose_name = 'numero de cuenta')
    date = models.CharField(max_length=10,blank=False, null = False, verbose_name = 'fecha')
    transaccion = models.CharField(max_length=250,blank=False, null = False, verbose_name = 'transaction')

    class Meta:
        db_table = 'transaction'
    
    def __str__(self):
        return self.account_number
    
    def __unicode__(self):
        return self.account_number
