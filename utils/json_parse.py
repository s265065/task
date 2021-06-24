import json

with open('duty.json') as json_file:
    data = json.load(json_file)

groups = []
users = []
duty_lists = []
days = []

i = 0
group = {"groupId": 0, "groupName": '', "monthName": '', "monthNumber": 0, "year": 0}

j = 0
user = {"userName": '', "userFullname": '', "userId": 0, "userEmail": '', "isOnDutyThisMonth": '', "userPhone": '',
        "userExt": '', "isOwner": '', "groupId": 0}

k = 0
duty_list = {"day": 0, "userId": 0, "isDuty": ''}
day = {}

for lst_item in data:
    for key, value in lst_item.items():
        if key == 'usersDutyList':
            gr_id = group["groupId"]
            group.pop("groupId")
            group_model = {"model": "task.group", "pk": gr_id, "fields": group}
            groups.append(group_model)
            group = {"groupId": 0, "groupName": '', "monthName": '', "monthNumber": 0, "year": 0}
            i += 1
            for inner_lst_item in value:
                for key, value in inner_lst_item.items():
                    if key == 'dutyDays':
                        user.update({"groupId": gr_id})
                        usr_id = user["userId"]
                        user.pop("userId")
                        user_model = {"model": "task.user", "pk": usr_id, "fields": user}
                        users.append(user_model)
                        user = {"userName": '', "userFullname": '', "userId": 0, "userEmail": '',
                                "isOnDutyThisMonth": '', "userPhone": '', "userExt": '', "isOwner": '', "groupId": 0}
                        j += 1
                        for inner_in_lst_item in value:
                            for key, value in inner_in_lst_item.items():
                                if key != "dayOfWeek":
                                    if key == "isDuty":
                                        if value == "false":
                                            value = False
                                        else:
                                            value = True
                                    duty_list.update({key: value})
                            duty_list.update({"userId": usr_id})
                            duty_list_model = {"model": "task.usersDutyList", "fields": duty_list}
                            duty_lists.append(duty_list_model)
                            duty_list = {"day": 0, "userId": 0, "isDuty": 0}
                            k += 1
                    else:
                        if key == "isOwner":
                            if value == "false":
                                value = False
                            else:
                                value = True
                        user.update({key: value})
        else:
            group.update({key: value})

DAYS_OF_WEEK = ["Чт", "Пт", "Сб", "Вс", "Пн", "Вт", "Ср"]
for i in range(30):
    day_model = {"model": "task.dutyDays", "pk": i + 1, "fields": {"dayOfWeek": DAYS_OF_WEEK[i % 7]}}
    days.append(day_model)

with open('../test_task/fixtures/group.json', 'w') as jsonfile:
    json.dump(groups, jsonfile)

with open('../test_task/fixtures/user.json', 'w') as jsonfile:
    json.dump(users, jsonfile)

with open('../test_task/fixtures/userDutyList.json', 'w') as jsonfile:
    json.dump(duty_lists, jsonfile)

with open('../test_task/fixtures/day.json', 'w') as jsonfile:
    json.dump(days, jsonfile)
