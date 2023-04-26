import uuid
from django.db import models

class TimeStampModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.

    Attributes
    ----------
    created_at : datetime
        A DateTime object that is populated by default when added
    updated_at : datetime
        A DateTime object that is populated by default when updated
    uuid : uuid
        A universally unique identifier.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)  
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, unique=True)

    class Meta:
        abstract = True
