from django.db import models

class Burger(models.Model):
    name = models.CharField(max_length=20) # 문자열
    price = models.IntegerField(default=0) # 숫자
    calories = models.IntegerField(default=0) # 숫자

    def __str__(self):
        return self.name