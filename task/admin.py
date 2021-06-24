from django.contrib import admin

# Register your models here.
from task.models import UsersDutyList, DutyDays, Group, User

admin.site.register(User)
admin.site.register(Group)
admin.site.register(DutyDays)
admin.site.register(UsersDutyList)
