import math

from django.db import models
from django.conf import settings

from lib_social.users.models import User


class Author(models.Model):

    name = models.CharField(
        'Name',
        max_length=200,
        help_text='Name',
        null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or ''


class Location(models.Model):

    location = models.CharField(
        'Location',
        max_length=200,
        help_text='Location',
        null=True, blank=True
    )

    def __str__(self):
        return self.location or ''


class Category(models.Model):

    title = models.CharField(
        'Title',
        max_length=200,
        help_text='Title',
        null=True, blank=True
    )

    level = models.CharField(
        'Level',
        max_length=200,
        help_text='Title',
        null=True, blank=True
    )

    image = models.ImageField(
        upload_to = 'images/categories/',
        default = 'images/categories/None/no-img.jpg'
    )
    
    def __str__(self):
        return self.title or ''


class Book(models.Model):

    author = models.ForeignKey(
        'Author',
        related_name='books',
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    title = models.CharField(
        'Title',
        max_length=200,
        help_text='Title',
        null=True, blank=True
    )

    image = models.ImageField(
        upload_to = 'images/books/',
        default = 'images/books/None/no-img.jpg'
    )

    category = models.ForeignKey(
        'Category',
        related_name='books',
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    pdf = models.FileField(
        'PDF',
        upload_to='documents/',
        help_text='PDF',
        null=True, blank=True
    )
    
    description = models.TextField(
        'Description',
        help_text='Description',
        blank=True)

    location = models.ManyToManyField(
        'Location',
        related_name='books',
    )

    booker = models.ForeignKey(
        User,
        related_name='booked',
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ({})'.format(self.title, self.author.name)

    @property
    def get_remamining_count(self):
        return self.locations.count()

    @property
    def get_rating(self):
        q = self.ratings.values_list('rating', flat=True)
        return int(math.ceil(sum(q)/q.count()))


class Rating(models.Model):

    user = models.ForeignKey(
        User,
        related_name='ratings',
        on_delete=models.CASCADE,
        null=True, blank=True)

    book = models.ForeignKey(
        Book,
        related_name='ratings',
        on_delete=models.CASCADE,
        null=True, blank=True)

    rating = models.IntegerField(default=0)


class Thread(models.Model):

    user = models.ForeignKey(
        User,
        related_name='threads',
        on_delete=models.CASCADE,
        null=True, blank=True)

    title = models.CharField(
        'Title',
        max_length=200,
        help_text='Title',
        null=True, blank=True
    )

    description = models.TextField(
        'Description',
        help_text='Description',
        blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
