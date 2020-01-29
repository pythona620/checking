from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger
from random import randint
__author__ = 'python'
LOGGER = getLogger(__name__)
class checkingSkill(MycroftSkill):
	stops = {"vizag","sec","hyd","abc"}
# 	upperBound = {"vizag","sec","hyd","abc"}
# 	answer = 0
# 	userGuess = 0
	def get_numerical_response(self, dialog):
		while True:
			val = self.get_response(dialog)
# 			try:
# 				val = int(val)
				return val
# 			except ValueError:
# 				self.speak_dialog("invalid.input")
# 			except:
# 				self.speak_dialog("input.error")
	@intent_handler(IntentBuilder("").require("NumberGuess").optionally("Play").optionally("Suggest"))
	def handle_start_game_intent(self, message):
		self.speak_dialog("start.game")
		# get lower bound
		lowerBound = self.get_numerical_response("get.lower")
		self.speak(lowerBound)
		# get upper bound
		upperBound = self.get_numerical_response("get.upper")
		self.speak(upperBound)
# 		answer = randint(lowerBound, upperBound)
# 		userGuess = lowerBound - 1
		while True:
        		source = lowerBound
        		if source in stops:
            			while True:
                			destination = upperBound
                			if destination in stops:
                    				return lowerBound, upperBound
                			else:
                    				self.speak("Could you please enter a valid destination stop")
                    				continue
        		else:
            			self.speak("Could you please enter a valid boarding point")
            		continue
	def stop(self):
		print("The sourceing point is "+ source+"and the destination is"+ destination)
# 		lowerBound, upperBound = 0, 100
# 		answer = 0
# 		userGuess = answer
		return True
def create_skill():
	return checkingSkill()
