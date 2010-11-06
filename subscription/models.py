#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _

class Subscription(models.Model):
	name = models.CharField(_('Nome'), max_length=100)
	cpf = models.CharField(_('Cpf'), max_length=11, unique=True)
	email = models.EmailField(_('E-mail'), unique=True)
	phone = models.CharField(_('Telefone'),  max_length=20, blank=True)
	created_at = models.DateTimeField(_('Criado em'),  auto_now_add=True)
	paid = models.BooleanField()
	
	def __unicode__(self):
		return '%s - %s \n' % (self.id, self.name)
		
	# class Meta:
		# verboso_name = _(n'Inscrição')
		# verboso_name_plural = _(n'Inscrições')
	