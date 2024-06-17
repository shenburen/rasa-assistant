from typing import Any, Text, Dict, List
from datetime import datetime, timedelta

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.common import date_to_int, int_to_weekend


class ActionFeatureTime(Action):
    def name(self) -> Text:
        return "action_feature_time"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        current = datetime.now().strftime("%H:%M:%S")
        dispatcher.utter_message(text=current)
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
        date = tracker.get_slot("date") or "今天"
        int = date_to_int(date)
        if int is not None:
            target = datetime.now() + timedelta(days=int)
            dispatcher.utter_message(text=target.strftime("%Y-%m-%d"))
        else:
            dispatcher.utter_message(text="系统暂不支持'{}'的日期查询".format(date))
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
        date = tracker.get_slot("date") or "今天"
        int = date_to_int(date)
        if int is not None:
            target = datetime.now() + timedelta(days=int)
            dispatcher.utter_message(text=int_to_weekend(target.weekday()))
        else:
            dispatcher.utter_message(text="系统暂不支持'{}'的星期查询".format(date))
        return []
