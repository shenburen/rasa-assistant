weekday_mapping = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期天"]

# 每个月的日数-闰年
month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def int_to_weekend(int):
    return weekday_mapping[int]


def date_to_int(text):
    if text == "今天":
        return 0
    elif text == "明天":
        return 1
    elif text == "后天":
        return 2
    elif text == "昨天":
        return -1
    elif text == "前天":
        return -2
    else:
        return None


def month_to_int(text):
    if text == "一月":
        return 1
    elif text == "二月":
        return 2
    elif text == "三月":
        return 3
    elif text == "四月":
        return 4
    elif text == "五月":
        return 5
    elif text == "六月":
        return 6
    elif text == "七月":
        return 7
    elif text == "八月":
        return 8
    elif text == "九月":
        return 9
    elif text == "十月":
        return 10
    elif text == "十一月":
        return 11
    elif text == "十二月":
        return 12


def type_to_int(text):
    if text == "打卡正常":
        return 0
    elif text == "打卡异常":
        return 1
    elif text == "缺卡":
        return 99
