from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from base.models import BookModel

User = get_user_model()


def image_path(instance, filename):
    return f'{instance.name}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField('firstname', max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True)
    favorite = models.TextField()
    bio = models.TextField()
    location = models.TextField()

    gender_choices = (
        ('m', 'male'),
        ('f', 'female')
    )
    _gender = models.CharField(choices=gender_choices, max_length=10, default='female')
    birth_date = models.DateField(null=True)
    image = models.ImageField(upload_to='')

    created_date = models.DateField(auto_now_add=True)

    @property
    def gender(self):
        return dict(self.gender_choices)[self._gender]

    @gender.setter
    def gender(self, gender_choice):
        reverse_gender = {v: k for k, v in dict(self.gender_choices).items()}
        self._gender = reverse_gender.get(gender_choice)

    def __str__(self):
        return f'{self.user.username}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class RegisteredBookModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}:{self.book.name}'
