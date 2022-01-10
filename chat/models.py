import jdatetime

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

User = get_user_model()


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True, null=True)
    seen = models.BooleanField(null=True, default=False)
    seen_datetime = models.DateTimeField(null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey

    def __str__(self):
        return self.message[:50]

    def is_customer(self):
        return 'customer' in [group.name for group in self.user.groups.all()]

    def is_operator(self):
        return not self.is_customer()

    def created_datetime_jd(self):

        jdatetime.datetime.now().strftime('%A %B')
        G2J = jdatetime.datetime.fromgregorian(
            year=self.created_datetime.year,
            month=self.created_datetime.month,
            day=self.created_datetime.day,
            hour=self.created_datetime.hour,
            minute=self.created_datetime.minute,
            second=self.created_datetime.second,
        )
        return G2J.strftime('%A, %d %B %y %H:%M:%S')
