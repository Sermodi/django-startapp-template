from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User

# Create your models here.
class <nombre_clase>(models.Model):
	name = models.CharField(
		_('nombre'),
		max_length=255,
	)
	description = models.TextField(
		_('descripcion'),
		blank=True,
		null=True,
	)
	user = models.ForeignKey(
		User,
		db_column= "usuario",
		parent_link= True,
		on_delete= models.CASCADE,
		related_name="usuario",
		unique= False,
		blank = False,
		null = False
	)
	created_at = models.DateTimeField(
		_("created_at"),
		auto_created=True
	)

	def __str__(self):
		return self.name