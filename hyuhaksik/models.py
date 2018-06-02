from django.db import models
# Create your models here.

class Menu(models.Model):
    cafe_name_choices = (
        ('SC','학생식당'),
        ('PC','교직원식당'),
        ('LR','사랑방'),
        ('NPC','신교직원식당'),
        ('NSC','신학생식당'),
        ('D1','제1 생활관'),
        ('D2','제2 활관'),
        ('HP','행원파크'),
    )
    id = models.AutoField(primary_key=True)
    op_time = models.CharField(max_length=30, default="")
    date = models.DateTimeField(auto_now=True)
    menu = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=30, default="")
    cafe_name = models.CharField(max_length=30, choices=cafe_name_choices)

    def __str__(self):
        return self.cafe_name
    def __str__(self):
        return self.date
    def __str__(self):
        return self.menu

class univ_site(models.Model):
    cafe_name_choices = (
        ('SC','학생식당'),
        ('PC','교직원식당'),
        ('LR','사랑방'),
        ('NPC','신교직원식당'),
        ('NSC','신학생식당'),
        ('D1','제1 생활관'),
        ('D2','제2 활관'),
        ('HP','행원파크'),
    )
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    cafe_name = models.CharField(max_length=30, choices=cafe_name_choices)
    def __str__(self):
        return self.cafe_name
    def __str__(self):
        return self.date
