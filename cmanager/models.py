from django.db import models


INTRO_CHOICES = (
    ('search', 'جست‌وجوی اینترنت'),
    ('friends', 'معرفی دوستان'),
    ('instagram', 'اینستاگرام'),
    ('roomiz', 'سایت رومیز'),
    ('events', 'شرکت در رویدادها'),
    ('other', 'سایر'),
)


class User(models.Model):
    fisrt_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=50, null=False)
    card_number = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=15, null=False)
    intro = models.CharField(max_length=50, choices=INTRO_CHOICES, default='other')
    year_of_birth = models.IntegerField(null=False)
    month_of_birth = models.IntegerField(null=False)
    day_of_birth = models.IntegerField(null=False)

    def __str__(self):
        return self.fisrt_name + " " + self.last_name


class Game(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=True, default="00:00")
    numbers = models.IntegerField(null=False)
    add_date = models.DateField(null=False)

    def __str__(self):
        return str(self.user.card_number)