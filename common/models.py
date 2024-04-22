from django.db import models


class CommonModel(models.Model):
    """Common Model Definition"""

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    # Do not want to push the data to the DB
    class Meta:
        abstract = True
