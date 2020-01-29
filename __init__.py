from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger

from random import randint

__author__ = 'python'
LOGGER = getLogger(__name__)


stops = {"vizag","hyd","sec","vijayawada"}
class NumberGuessSkill(MycroftSkill):

# 	def get_numerical_response(self, dialog):
# 		while True:
# 			val = self.get_response(dialog)
# 	def get_stops(self, stops):
# 		stoplist = []
# 		if stops !=lower:
# 			self.speak(tested ok)
		
	@intent_handler(IntentBuilder("").require("NumberGuess").optionally("Play").optionally("Suggest"))
# 	def handle_start_game_intent(self, message):
# 		self.speak_dialog("start.game")
	def get_numerical_response(self, dialog):
# 		# get lower bound
		lowerBound = self.get_numerical_response("get.lower")
# 		# get upper bound
		upperBound = self.get_numerical_response("get.upper")
		if lowerBound is not None:
			self.speak(lowerBound + " "+upperBound)
        		else:
            		     self.speak('you are not given any specific word!')
	def stop(self):
		pass

def create_skill():
	return NumberGuessSkill()
