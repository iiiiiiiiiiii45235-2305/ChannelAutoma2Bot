from django.db import models
from django_extensions.db.models import TimeStampedModel


class Reaction(TimeStampedModel):
    reaction = models.fields.CharField(max_length=100)
    message = models.fields.BigIntegerField()
    users = models.ManyToManyField('UserSettings', related_name='reactions', blank=True)
    channel = models.ForeignKey('ChannelSettings', on_delete=models.CASCADE, null=True)

    bot_token = models.fields.CharField(max_length=200)

    def __str__(self):
        return f'{self.reaction}@{self.channel_id}:{self.message}'
