from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger
from random import randint
__author__ = 'pthona'
LOGGER = getLogger(__name__)
class NumberGuessSkill(MycroftSkill):
	sor = []
	des = []
	def get_name_response(self,dialog):
	def get_name_response(self,dialog):
# 	lowerBound = 0
# 	upperBound = 100
# 	answer = 0
# 	userGuess = 0
# 	def get_numerical_response(self, dialog):
# 	def get_numerical_response(self, dialog):
# 		while True:
# 			val = self.get_response(dialog)
# 			try:
# 				val = int(val)
# 				return val
# 			except ValueError:
# 				self.speak_dialog("invalid.input")
# 			except:
# 				self.speak_dialog("input.error")
	@intent_handler(IntentBuilder("").require("NumberGuess").optionally("Play").optionally("Suggest"))
	def handle_start_game_intent(self, message):
		self.speak_dialog("start.game")
		# get lower bound
		lowerBound = get_name_response("get.sor")
		# get upper bound
		upperBound = get_name_response("get.des")
		
		if lowerBound is not None:
			self.speak(lowerBound + " "+upperBound)
# 		answer = randint(lowerBound, upperBound)
# 		userGuess = lowerBound - 1
# 		while userGuess != answer:
# 			userGuess = self.get_numerical_response("guess")
# 			if userGuess < answer:
# 				self.speak_dialog("too.low")
# 			elif userGuess > answer:
# 				self.speak_dialog("too.high")
# 		self.speak_dialog("correct")
	def stop(self):
		pass
# 		lowerBound, upperBound = 0, 100
# 		answer = 0
# 		userGuess = answer
# 		return True
def create_skill():
	return NumberGuessSkill()
