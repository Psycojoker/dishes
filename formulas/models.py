from django.db import models

class Formula(models.Model):
    name = models.CharField(max_length=255)
    #author = models.ForeignKey('User') 
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
