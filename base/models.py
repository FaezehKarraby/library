from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from chat.models import Chat


def image_path(instance, filename):
    return instance.name


def attachment_path(instance, filename):
    return instance.name


class GenreModel(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to=image_path, null=True)
    slug = models.SlugField(null=True, blank=True)
    chat = GenericRelation(Chat)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-')
        super().save(*args, **kwargs)


class AuthorModel(models.Model):
    class Meta:
        ordering = ['name']

    genre = models.ManyToManyField('GenreModel')
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to=image_path, null=True)
    slug = models.SlugField(null=True, blank=True)
    gender_choice = (
        ('m', 'male'),
        ('f', 'female'),
    )
    gender = models.CharField(choices=gender_choice, max_length=10, default='male')

    birth_date = models.DateField(null=True)

    attachment_files = GenericRelation('AttachmentFiles')
    chat = GenericRelation(Chat)

    def __str__(self):
        return f'{self.name}'

    def get_genre(self):
        genres = []
        for genre1 in self.genre.all():
            genres.append(genre1)
        return genres

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-')
        super().save(*args, **kwargs)


class BookModel(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=255, null=True)
    author = models.ForeignKey('AuthorModel', on_delete=models.CASCADE)
    publisher = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=255, null=True)
    translator = models.CharField(max_length=255, default='None')
    production_year = models.DateField(null=True)
    pages = models.IntegerField(default=0)
    description = RichTextUploadingField(null=True)
    image = models.ImageField(upload_to=image_path, null=True)
    slug = models.SlugField(null=True, blank=True)

    attachment_files = GenericRelation('AttachmentFiles')
    chat = GenericRelation(Chat)


    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('base:book_details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-')
        super().save(*args, **kwargs)


class AttachmentFiles(models.Model):
    class Meta:
        ordering = ['file']

    file = models.FileField(upload_to='attach_files/%y-%m-%d_%H:%M')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        if self.content_type == 'BookModel':
            return 'book'
        return f'{self.content_object.name}'

    @property
    def name(self):
        return self.file.url.split('/')[-1]

    @property
    def color(self):
        color = {
            'png': 'cyan darken-4',
            'jpg': 'cyan darken-4',
            'tif': 'cyan darken-4',
            'doc': 'blue',
            'docx': 'blue',
            'ppt': 'red darken-2',
            'pptx': 'red darken-2',
            'csv': 'green darken-3',
            'xls': 'green darken-3',
            'xlsx': 'green darken-3',
            'zip': 'yellow lighten-1',
            'rar': 'yellow lighten-1',
            'json': 'black',
            'pdf': 'red',
        }
        file_format = self.name.split('.')[-1]

        return color.setdefault(file_format, 'orange')
