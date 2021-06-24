from django.db import models


class Group(models.Model):
    groupId = models.PositiveSmallIntegerField(primary_key=True)
    groupName = models.CharField(max_length=80)
    monthName = models.CharField(max_length=8)
    monthNumber = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()


class User(models.Model):
    userName = models.CharField(max_length=20)
    userFullname = models.CharField(max_length=60)
    userId = models.PositiveSmallIntegerField(primary_key=True)
    userEmail = models.EmailField(unique=True)
    isOnDutyThisMonth = models.BooleanField(default=False)
    userPhone = models.CharField(max_length=15)
    userExt = models.CharField(max_length=10)
    isOwner = models.BooleanField(default=False)
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)


class DutyDays(models.Model):
    DAYS_OF_WEEK = (
        ('Пн', 'Понедельник'),
        ('Вт', 'Вторник'),
        ('Ср', 'Среда'),
        ('Чт', 'Четверг'),
        ('Пт', 'Пятница'),
        ('Сб', 'Суббота'),
        ('Вс', 'Воскресенье'),
    )

    day = models.PositiveSmallIntegerField(primary_key=True)
    dayOfWeek = models.CharField(max_length=2, choices=DAYS_OF_WEEK)


class UsersDutyList(models.Model):
    day = models.ForeignKey(DutyDays, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    isDuty = models.BooleanField(default=False)
