from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger
from random import randint
__author__ = 'python'
LOGGER = getLogger(__name__)
class checkingSkill(MycroftSkill):
# 	stops = {"vizag","sec","hyd","abc"}
	def get_numerical_response(self, dialog):
		while True:
			val = self.get_response(dialog)
				return val
	@intent_handler(IntentBuilder("").require("travel").optionally("Play").optionally("Suggest"))
	def handle_start_game_intent(self, message):
		self.speak_dialog("start.game")
		# get lower bound
		lowerBound = self.get_numerical_response("get.lower")
		# get upper bound
		upperBound = self.get_numerical_response("get.upper")
# 	def  enter_source_destination(stops):
# 		while True:
#         		source = lowerBound
#         		if source in stops:
#             			while True:
#                 			destination = upperBound
#                 			if destination in stops:
#                     				return source, destination
#                 			else:
#                     				self.speak('Could you please enter a valid destination stop')
#                     				continue
#        			 else:
#             			self.speak('Could you please enter a valid boarding point')
#            			continue

# 	stops = {"vizag", "hyderabad", "vijayawada"}
# 	source, destination = enter_source_destination(stops)
# 	self.speak('The sourceing point is '+ source+ 'and the destination is '+ destination)

	def stop(self):
		return
def create_skill():
	return checkingSkill()
