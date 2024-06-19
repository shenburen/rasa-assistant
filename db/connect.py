import mysql.connector
import json
from datetime import datetime, timedelta

from actions.common import month_days

db = mysql.connector.connect(
    host="localhost", user="root", password="shenzhiqiang", database="test"
)


def get_clock_in(user, month):

    sql = "select start_time,end_time,type from sys_check_in_work w left join sys_user u on w.user_id = u.user_id where 1 = 1"
    sql += " and u.nick_name = '" + user + "'"
    sql += " and start_time >= '2024-" + str(month) + "-1'"
    sql += " and end_time < '2024-" + str(month + 1) + "-1'"
    sql += " order by start_time"

    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()

    data = {"type": "echarts-calendar", "month": "2024-" + str(month), "list": []}

    row_index = 0
    for i in range(0, month_days[month - 1]):

        if len(rows) <= row_index:
            break

        obj_date = datetime.strptime(
            "2024-" + str(month) + "-" + str(i + 1), "%Y-%m-%d"
        )
        normal_date = obj_date.strftime("%Y-%m-%d")
        record_date = rows[row_index][0].strftime("%Y-%m-%d")

        if normal_date == record_date:
            if rows[row_index][2] == "0":
                data["list"].append([normal_date, "正常"])
            else:
                data["list"].append([normal_date, "异常"])
            row_index += 1
        else:
            if obj_date.weekday() == 5 or obj_date.weekday() == 6:
                data["list"].append([normal_date, ""])
            else:
                data["list"].append([normal_date, "缺卡"])

    return json.dumps(data, ensure_ascii=False)
