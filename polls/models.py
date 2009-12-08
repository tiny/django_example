# -*- coding: utf-8 -*-
import datetime
from django.db import models

# Create your models here.
class Poll(models.Model):
  """
  Модель голосования
  """
  question = models.CharField(max_length=200)
  pub_date = models.DateTimeField('Дата публикации')

  def __unicode__(self):
    return self.question

  def was_published_today(self):
    """Голосование опубликовано сегодня?"""
    return self.pub_date.date() == datetime.date.today()
  was_published_today.short_description = 'Published today?'


class Choice(models.Model):
  """
  Модель выбора голосования
  """
  poll = models.ForeignKey(Poll)
  choice = models.CharField(max_length=200)
  votes = models.IntegerField()

  def __unicode__(self):
    return self.choice
