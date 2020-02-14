from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    times = models.IntegerField("剩余抽奖次数", default=0)
    money = models.IntegerField("可找子哲兑换的奖金", default=0)
    spirit_reward = models.CharField("精神奖励",max_length=3000,default="")