from django.db import models


class AlbumTitle(models.Model):
    albumTitle = models.CharField(max_length=300, default='')

    def __str__(self):
        return '{0}'.format(self.albumTitle)
class Pic(models.Model):
    id = models.AutoField(primary_key=True)
    albumTitle = models.ForeignKey(AlbumTitle, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def __str__(self):
        return '{0}. {1}'.format(self.id, self.albumTitle)
