from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger

from random import randint

__author__ = 'python'
LOGGER = getLogger(__name__)

class NumberGuessSkill(MycroftSkill):

	def get_numerical_response(self, dialog):
		while True:
			val = self.get_response(dialog)
			
	@intent_handler(IntentBuilder("").require("NumberGuess").optionally("Play").optionally("Suggest"))
	def handle_start_game_intent(self, message):
		self.speak_dialog("start.game")

		# get lower bound
		lowerBound = self.get_numerical_response("get.lower")
		# get upper bound
		upperBound = self.get_numerical_response("get.upper")

	def stop(self):
		pass

def create_skill():
	return NumberGuessSkill()
