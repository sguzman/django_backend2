from django.db import models


# Create your models here.
class ChanStats(models.Model):
    time = models.DateTimeField(primary_key=True)
    serial = models.CharField(max_length=24)
    subs = models.BigIntegerField()
    videos = models.IntegerField()
    views = models.BigIntegerField()

    class Meta:
        db_table = 'chan_stats'
