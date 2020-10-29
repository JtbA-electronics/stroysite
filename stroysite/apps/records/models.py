from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField('Название',max_length=200)
	text = models.TextField('Текст')
	created_date = models.DateTimeField('Дата создания',default=timezone.now)
	published_date = models.DateTimeField('Дата публикации',blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	class  Meta(object):
		verbose_name = 'Запись'
		verbose_name_plural = 'Записи'