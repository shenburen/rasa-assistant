import mysql.connector
from datetime import datetime, timedelta

"""
插入测试数据的工具脚本
"""
db = mysql.connector.connect(
    host="localhost", user="root", password="shenzhiqiang", database="test"
)


date_str = "2023-12-31"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")


for i in range(1, 367):
    new_date_obj = date_obj + timedelta(days=i)
    new_date_str = new_date_obj.strftime("%Y-%m-%d")

    cursor = db.cursor()
    cursor.execute(
        "insert into sys_check_in_work set id="
        + str(i)
        + ",user_id=131,start_time='"
        + new_date_str
        + " 9:00:00',end_time='"
        + new_date_str
        + " 18:00:00',type="
        + str(i % 2)
        + ";"
    )

    db.commit()
    cursor.close()

db.close()
