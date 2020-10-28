# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Text, Dict, List

from rasa_sdk import Tracker
from typing import Text, Dict, List

from rasa_sdk import Tracker

form
rasa_sdk.forms
import FormAction


class SoftskillsForm(FormAction):

    def name(self) -> Text:
        return "softskills_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["skills", "personally", "problems_dealing", "public"]

    def slot_mapping(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "skills": self.from_entities(entity="skills"),
            "personally": [
                self.from_entities(entity="personally"),
                self.from_entities(entity="number"),
            ],
            "problems_dealing": [
                self.from_entities(entity="problems_dealing"),
            ],
            "public": [
                self.from_entities(entity="public"),
            ]

        }
