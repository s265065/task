from django.db import connection
from django.shortcuts import render

from task.models import User, Group, DutyDays, UsersDutyList


def index(request):
    # users = User.objects.all()
    users = None
    return render(request, "index.html", {"users": users})


def get(request):
    gr_id = request.POST.get("groupId")
    day = request.POST.get("day")

    print(day, gr_id)

    if gr_id != "all":
        sql = 'SELECT userName, userEmail, userPhone FROM task_user ' \
              'JOIN task_group ON task_user.groupId_id = task_group.groupId ' \
              'JOIN task_usersdutylist ON task_user.userId = task_usersdutylist.userId_id ' \
              'WHERE (groupId = %s) AND (day_id = %s) AND (isDuty = true)'
        cursor = connection.cursor()
        cursor.execute(sql, [gr_id, day])

    else:
        sql = 'SELECT userName, userEmail, userPhone FROM task_user ' \
            'JOIN task_group ON task_user.groupId_id = task_group.groupId ' \
            'JOIN task_usersdutylist ON task_user.userId = task_usersdutylist.userId_id ' \
            'WHERE (day_id = %s) AND (isDuty = true)'
        cursor = connection.cursor()
        cursor.execute(sql, [day])

    desc = cursor.description
    users = [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

    for i in range(1, 31):
        sql = 'SELECT userName, userEmail, userPhone FROM task_user ' \
              'JOIN task_group ON task_user.groupId_id = task_group.groupId ' \
              'JOIN task_usersdutylist ON task_user.userId = task_usersdutylist.userId_id ' \
              'WHERE (day_id = %s) AND (isDuty = true)'
        cursor = connection.cursor()
        cursor.execute(sql, [day])

        desc = cursor.description
        table = [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]

    return render(request, "index.html", {"users": users, "table": table})

