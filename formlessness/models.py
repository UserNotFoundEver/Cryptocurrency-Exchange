from django.db import models


class Formless(models.Model):
    input = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Processing(models.Model):
    recipient_address = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Payment(models.Model):
    pass
