from django.db import models
from django.conf import settings


# Create your models here.
class WBText(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者')
    text = models.TextField(max_length=140, verbose_name='微博')

    def __str__(self):
        return self.text[:10]


class WeiBo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_del = models.BooleanField(default=False, verbose_name='是否删除')
    text = models.ForeignKey(WBText, verbose_name='文本')

    def del_this(self):
        self.is_del = True
        self.save()

    def comment_this(self, user: settings.AUTH_USER_MODEL, text: str):
        """
        评论微博
        """
        comment = Comment.objects.create(target=self, user=user, text=text)
        return comment

    def __str__(self):
        return self.text.__str__()


    class Meta:
        ordering = ['-create_time', 'text']



class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户')
    target = models.ForeignKey(WeiBo, verbose_name='微博')
    create_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=100, verbose_name='评论')
    is_del = models.BooleanField(verbose_name='是否删除', default=False)

    def __str__(self):
        return self.text[:10]

    def del_this(self):
        self.is_del = True
        self.save()
