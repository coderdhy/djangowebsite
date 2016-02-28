from django.db import models

# Create your models here.


class FileInfo(models.Model):
    fileid = models.CharField(primary_key=True, max_length=50)
    filename = models.CharField(max_length=255)
    filepath = models.CharField(max_length=255)
    fileext = models.CharField(max_length=10)
    filesize = models.IntegerField()
    sizecomplete = models.IntegerField(default=0)
    uploadtime = models.DateTimeField(auto_now_add=True)
    bcomplete = models.BooleanField(default=False)


