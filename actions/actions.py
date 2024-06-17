from typing import Any, Text, Dict, List
from datetime import datetime, timedelta

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from db.connect import get_userid


def text_date_to_int(text_date):
    if text_date == "今天":
        return 0
    if text_date == "明天":
        return 1
    if text_date == "昨天":
        return -1

    # in other case
    return None


weekday_mapping = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期天"]


def weekday_to_text(weekday):
    return weekday_mapping[weekday]


class ActionFeatureTime(Action):
    def name(self) -> Text:
        return "action_feature_time"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        current_time = datetime.now().strftime("%H:%M:%S")
        dispatcher.utter_message(text=current_time)

        return []


class ActionFeatureDate(Action):
    def name(self) -> Text:
        return "action_feature_date"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        text_date = tracker.get_slot("date") or "今天"

        int_date = text_date_to_int(text_date)
        if int_date is not None:
            delta = timedelta(days=int_date)
            current_date = datetime.now()

            target_date = current_date + delta

            dispatcher.utter_message(text=target_date.strftime("%Y-%m-%d"))
        else:
            dispatcher.utter_message(
                text="系统暂不支持'{}'的日期查询".format(text_date)
            )

        return []


class ActionFeatureWeekday(Action):
    def name(self) -> Text:
        return "action_feature_weekday"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        text_date = tracker.get_slot("date") or "今天"

        int_date = text_date_to_int(text_date)
        if int_date is not None:
            delta = timedelta(days=int_date)
            current_date = datetime.now()

            target_date = current_date + delta

            dispatcher.utter_message(text=weekday_to_text(target_date.weekday()))
        else:
            dispatcher.utter_message(
                text="系统暂不支持'{}'的星期查询".format(text_date)
            )

        return []


class ActionServiceUser(Action):
    def name(self) -> Text:
        return "action_service_user"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        text_user = tracker.get_slot("user")
        id = get_userid(text_user)
        dispatcher.utter_message(text=id)
        return []
