import time

from django.db import models


class Job(models.Model):
    TYPE_SLOW = "slow"
    TYPE_FAST = "fast"
    TYPES = (
        (TYPE_SLOW, "Slow job"),
        (TYPE_FAST, "Fast job"),
    )

    STATUS_PENDING = "pending"
    STATUS_DONE = "done"
    STATUSES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_DONE, "Done"),
    )

    type = models.CharField(
        max_length=4,
        choices=TYPES,
    )
    status = models.CharField(
        max_length=7,
        choices=STATUSES,
        default=STATUS_PENDING,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def process(self):
        if self.type == Job.TYPE_SLOW:
            time.sleep(30)
        elif self.type == Job.TYPE_FAST:
            time.sleep(1)
        else:
            raise ValueError("Unknown job type.")
