# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcherfrom typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message("Hello World!")
#         return []


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message("Hello World!")
#         return []


from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from typing import Dict, Text, Any, List, Union, Optional

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT


class ActionCheckRestaurants(Action):
    def name(self):
        # type: () -> Text
        return "action_check_restaurants"

    def run(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]
        #cuisine = tracker.get_slot('name')
        #q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
        #result = db.query(q)
        result = "Let me show you some restaurents"
        return [SlotSet("matches", result)]

class Quoteform(FormAction):
    def name(self):
        return "quote_form"
        
    @staticmethod
    def required_slot(tracker:Tracker)->List[Text]:
        return (["project_name","project_use","idea","application","money","contact"])
    
    def submit(self,dispatcher : CollectingDispatcher,tracker:Tracker,domain :Dict[Text,Any]) -> List[Dict]:
        dispatcher.utter_template('utter_send',tracker)
        return []