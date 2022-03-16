import datetime as dt 
import requests as rq
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"La hora es: {dt.datetime.now()}")

        return []


class ActionApi(Action):

    def name(self) -> Text:
        return "action_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        x = rq.get('https://www.zaragoza.es/sede/servicio/monumento.geojson?srsname=wgs84&rows=1&fl=id,title,description,geometry');
        

        dispatcher.utter_message(text=f"El monumento es: "+str(x.json()['features'][0]['properties']['title']))

        return []
