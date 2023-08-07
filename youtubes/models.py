from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Video (models.Model):
    video = models.URLField(blank=True , null= True , verbose_name="Video Url")
    title = models.CharField(max_length=500)
    author = models.ForeignKey(User , related_name='user_video' , on_delete=models.CASCADE )
    crate_date = models.DateTimeField( default= timezone.now() ,blank=True)
    likes = models.ManyToManyField(User, related_name='video_like')
    dislikes = models.ManyToManyField(User, related_name='video_dislike')
    tags = TaggableManager()
    views  = models.IntegerField(default=0)
    def __str__(self ):
        return self.title


class Comment(models.Model):

    content = models.TextField (max_length=1500)
    crate_date = models.DateTimeField(default= timezone.now(), blank=True)
    user = models.ForeignKey(User , related_name='comment_user', on_delete=models.CASCADE)
    video = models.ForeignKey(Video , related_name='comment_video', on_delete=models.CASCADE)
    def __str__(self ):
        return str(self.user)
