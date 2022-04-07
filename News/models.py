from email.policy import default
from django.db import models
from django.urls import reverse
from django.forms import forms
#create your models here

class Category(models.Model):
	title = models.CharField(max_length=100)
	category_image = models.ImageField(upload_to='category/image')
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Author(models.Model):
	name = models.CharField(max_length=100, blank=False)
	address = models.CharField(max_length=100)
	email = models.EmailField()
	image = models.ImageField(upload_to='author/images')
	date  = models.DateTimeField()
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{}".format(self.name)

	def get_absolute_url(self):
		return reverse("News:create-author", kwargs={'id':self.id})


class News(models.Model):
	category=models.ForeignKey(Category, on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	image=models.ImageField(upload_to='news/imgs')
	date = models.DateTimeField()
	details=models.TextField()
	date_created=models.DateTimeField(auto_now_add=True)
	

	def __str__(self):
		return "{} -> {}".format(self.category, self.title)

	


class Comment(models.Model):
	author=models.ForeignKey(Author, on_delete=models.CASCADE)
	news=models.ForeignKey(News, on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	comment=models.TextField()
	status=models.BooleanField(default=False)

	def __str__(self):
		return self.name