# from typing import Any, Text, Dict, List
#
# from rasa_sdk.events import SlotSet
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionReceiveslots(Action):
#
#     def name(self) -> Text:
#         return "action_receive_elementname"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         text = tracker.latest_message['text']
#         dispatcher.utter_message(text=f"I'll remember your elementname as {text}!")
#         return [SlotSet("elementname", text)]
#
#
# class ActionReceiveslotsxpath(Action):
#
#     def name(self) -> Text:
#         return "action_receive_xpath"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         text = tracker.latest_message['text']
#         dispatcher.utter_message(text=f"I'll remember your xpath as {text}!")
#         return [SlotSet("xpath", text)]
#
#
# class ActionReceiveslotsmaxsize(Action):
#
#     def name(self) -> Text:
#         return "action_receive_maxsize"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         text = tracker.latest_message['text']
#         dispatcher.utter_message(text=f"I'll remember your maximum field size as {text}!")
#         return [SlotSet("maxsize", text)]
#
#
# class ActionReceiveslotsminsize(Action):
#
#     def name(self) -> Text:
#         return "action_receive_minsize"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         text = tracker.latest_message['text']
#         dispatcher.utter_message(text=f"I'll remember your minimum field size as {text}!")
#         return [SlotSet("minsize", text)]
#
#
# class ActionReceiveslotsallowabledatatypes(Action):
#
#     def name(self) -> Text:
#         return "action_receive_allowabledatatypes"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         text = tracker.latest_message['text']
#         dispatcher.utter_message(text=f"I'll remember your allowable data types  as {text}!")
#         return [SlotSet("allowabledatatypes", text)]
#
#
# class ActionReceiveslotsnonallowabledatatypes(Action):
#
#     def name(self) -> Text:
#         return "action_receive_nonallowabledatatypes"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         text = tracker.latest_message['text']
#         dispatcher.utter_message(text=f"I'll remember your non-allowable datatypes data types  as {text}!")
#         return [SlotSet("nonallowabledatatypes", text)]
#
#
# class ActionSayELEMENTName(Action):
#
#     def name(self) -> Text:
#         return "action_say_elementname"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         elementname = tracker.get_slot("elementname")
#         if not elementname:
#             dispatcher.utter_message(text="I don't know elementname")
#         else:
#             dispatcher.utter_message(text=f"Your element name is {elementname}!")
#         return []
#
#
# class ActionSayXPATHName(Action):
#
#     def name(self) -> Text:
#         return "action_say_xpath"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         xpath = tracker.get_slot("xpath")
#         if not xpath:
#             dispatcher.utter_message(text="I don't know xpath")
#         else:
#             dispatcher.utter_message(text=f"Your xpath is {xpath}!")
#         return []
#
#
# class ActionSayMAXSIZE(Action):
#
#     def name(self) -> Text:
#         return "action_say_maxsize"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         maxsize = tracker.get_slot("maxsize")
#         if not maxsize:
#             dispatcher.utter_message(text="I don't know maxsize")
#         else:
#             dispatcher.utter_message(text=f"Maximum field length  is {maxsize}!")
#         return []
#
#
# class ActionSayMinSIZE(Action):
#
#     def name(self) -> Text:
#         return "action_say_minsize"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         minsize = tracker.get_slot("minsize")
#         if not minsize:
#             dispatcher.utter_message(text="I don't know minsize")
#         else:
#             dispatcher.utter_message(text=f"Minimum field length  is {minsize}!")
#         return []
#
#
# class ActionSayAllowableSize(Action):
#
#     def name(self) -> Text:
#         return "action_say_allowabledatatypes"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         allowabledatatypes = tracker.get_slot("allowabledatatypes")
#         if not allowabledatatypes:
#             dispatcher.utter_message(text="I don't know allowable data types for this field")
#         else:
#             dispatcher.utter_message(text=f"allowable data types for this field is {allowabledatatypes}!")
#         return []
#
#
# class ActionSayNONAllowableSize(Action):
#
#     def name(self) -> Text:
#         return "action_say_nonallowabledatatypes"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         nonallowabledatatypes = tracker.get_slot("nonallowabledatatypes")
#         if not nonallowabledatatypes:
#             dispatcher.utter_message(text="I don't know non-allowable data types for this field")
#         else:
#             dispatcher.utter_message(text=f"Non-Allowable data types for this field is {nonallowabledatatypes}!")
#         return []
