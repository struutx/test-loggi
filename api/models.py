import uuid

from django.db import models


class User(models.Model):
    """
    Model to represent a User on Database
    """
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'
