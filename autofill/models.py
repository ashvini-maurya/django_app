from django.db import models

class User(models.Model):
  city = models.CharField(max_length=128)
  state = models.CharField(max_length=128)
  country = models.CharField(max_length=128)

  def __unicode__(self):
    return self.city
