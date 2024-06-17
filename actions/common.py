weekday_mapping = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期天"]


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
