import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", password="shenzhiqiang", database="test"
)


def get_userid(user):
    cursor = db.cursor()
    cursor.execute("select * from sys_user where nick_name = '" + user + "'")
    row = cursor.fetchall()

    if len(row) == 1:
        return str(row[0][0])
    else:
        return ""
