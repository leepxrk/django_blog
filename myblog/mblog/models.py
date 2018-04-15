from django.db import models
from django.utils import timezone
import imp,sys,re

# Create your models here.

#imp.reload(sys)
#sys.setdefaultencoding('utf8')
# python 3 默认编码unicode，所以这一行就不需要了

class musician(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    insturment = models.CharField(max_length = 100)

class Album(models.Model):
    artist = models.ForeignKey(musician,on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class post(models.Model):
    title = models.CharField(max_length = 50)
    tag = models.CharField(max_length = 50)
    body = models.TextField()
    pub_date = models.DateTimeField(default = timezone.now)