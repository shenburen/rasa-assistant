from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.common import month_to_int, type_to_int
from db.connect import get_clock_in


class ActionServiceUser(Action):
    def name(self) -> Text:
        return "action_service_user"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user = tracker.get_slot("clock_in_user")
        month = month_to_int(tracker.get_slot("clock_in_month"))
        data = get_clock_in(user, month)
        dispatcher.utter_message(text=data)
        return []
