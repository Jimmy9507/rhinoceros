from django.db import models

# Create your models here.
class Article(models.Model):
    #标题
    title=models.CharField(max_length=32,default='Title')
    #内容
    content=models.TextField(null=True)
    pub_time=models.DateTimeField(null=True   )
    def __unicode__(self):
        return self.title