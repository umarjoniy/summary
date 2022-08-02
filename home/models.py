from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=75)
    about = models.CharField(max_length=150)
    text = models.TextField(max_length=200)
    image = models.ImageField(upload_to='medias')

    def __str__(self):
        return self.name


class ServicesText(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Partners(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='partners')
    place = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='me')
    birthday = models.DateField()
    address = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    email = models.EmailField()
    website = models.URLField()
    phone = models.CharField(max_length=25)
    completed = models.IntegerField()
    partners = models.ManyToManyField(Partners)

    def __str__(self):
        return self.name


class Education(models.Model):
    period = models.CharField(max_length=50)
    title = models.CharField(max_length=75)
    name = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='education', blank=True)
    place = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Experience(models.Model):
    period = models.CharField(max_length=75)
    title = models.CharField(max_length=75)
    name = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='experience', blank=True)
    place = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Skills(models.Model):
    name = models.CharField(max_length=50)
    num = models.IntegerField()
    is_main = models.BooleanField(default=False)
    lwnum = models.IntegerField(blank=True, default=None, null=True)
    lmnum = models.IntegerField(blank=True, default=None, null=True)

    def __str__(self):
        return self.name


class Awards(models.Model):
    period = models.CharField(max_length=75)
    title = models.CharField(max_length=75)
    name = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='awards', blank=True)
    place = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=50)
    context = models.TextField()
    ico = models.ImageField(upload_to='services', blank=True)
    text_ico = models.ForeignKey(ServicesText, on_delete=models.CASCADE, null=True)
    place = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Projects(models.Model):
    image = models.ImageField(upload_to='projects')
    name = models.CharField(max_length=75)
    field = models.ForeignKey(Skills, on_delete=models.CASCADE)
    place = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Another(models.Model):
    awards = models.IntegerField()
    projects = models.IntegerField()
    customers = models.IntegerField()
    coffee = models.IntegerField()


class Posts(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    content = RichTextField(null=True)
    paragraph = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts', null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    slug = models.SlugField(blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comments(models.Model):
    article = models.ForeignKey(Posts, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    message = models.TextField()
    email = models.EmailField()
    website = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.name



@receiver(pre_save, sender=Posts)
def article_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)