from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from db.connect import get_data, get_userid


class ActionQueryUser(Action):
    def name(self) -> Text:
        return "action_query_user"

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
