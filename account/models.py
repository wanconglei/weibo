from django.db import models
from django.contrib.auth.models import AbstractUser
from weibo.models import WeiBo, WBText


# Create your models here.
class WBUser(AbstractUser):
    GENDER_OPTIONS = (
        (0, '保密'),
        (1, '男'),
        (2, '女'),
        (3, '其他')
    )
    nickname = models.CharField(verbose_name='昵称', max_length=60, null=True, blank=True)
    gender = models.IntegerField(verbose_name='性别', choices=GENDER_OPTIONS, default=0)
    _info = models.TextField(verbose_name='其他信息', blank=True, null=True)
    # ManyToManyField 的首个参数指定被关联的类，
    # 此处 WBUser 尚未定义完成，可用字符串形式“临时”代替，正式添加 followers 时，django 会自动替换为 WBUser 对象
    followers = models.ManyToManyField('WBUser', verbose_name='粉丝')

    def __str__(self):
        return self.nickname or self.username

    def update(self, text: str):
        wbt = WBText.objects.create(author=self, text=text)
        wb = WeiBo.objects.create(user=self, text=wbt)
        return wb

    class Meta:
        ordering = ['-id', 'username']

