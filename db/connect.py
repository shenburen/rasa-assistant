import mysql.connector
import json

from actions.common import month_days

db = mysql.connector.connect(
    host="localhost", user="root", password="shenzhiqiang", database="test"
)


def get_clock_in(user, month, type):

    sql = "select start_time,end_time,type from sys_check_in_work w left join sys_user u on w.user_id = u.user_id where 1 = 1"
    sql += " and u.nick_name = '" + user + "'"
    sql += " and start_time >= '2024-" + str(month) + "-1'"
    sql += " and end_time < '2024-" + str(month + 1) + "-1'"
    if type == 0 or type == 1:
        sql += " and type = " + str(type)
    sql += " order by start_time"

    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()

    data = {"type": "echart", "list": []}
    if type == 99:
        for item in rows:
            print(item)
    else:
        for item in rows:
            data["list"].append(
                {
                    "startTime": item[0].strftime("%Y-%m-%d %H:%M:%S"),
                    "endTime": item[1].strftime("%Y-%m-%d %H:%M:%S"),
                    "type": item[2],
                }
            )

    return json.dumps(data, ensure_ascii=False)
