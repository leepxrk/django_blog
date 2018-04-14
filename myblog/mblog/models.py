from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField(max_legth = 200)
    slug = models.CharField(max_lenth = 200)
    body = models.Textfield()
    pub_date = models.DateTimefield(default=timezone.now)

    class Meta:
        ordering = ('-pub_date')

    def__unicode__(self)
        return self.title