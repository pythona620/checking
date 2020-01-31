from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger
from random import randint
__author__ = 'python'
LOGGER = getLogger(__name__)
class checkingSkill(MycroftSkill):
	def get_stops(self, dialog):
		yip = self.get_response(dialog) 
		return yip
	@intent_handler(IntentBuilder("").require("travel").optionally("Play").optionally("Suggest"))
	def handle_start_game_intent(self, message):
		self.speak_dialog("start.game")
		# get lower bound
		lowerBound = self.get_stops("get.lower")
		# get myfriendname
		upperBound = self.get_stops("get.upper")
	def  enter_source_destination(self,stops):
# 		stopslist = stpos.split(',')
# 		stopslist = []
		while True:
			source = lowerBound
	        	if source in stops:
				while True:
					destination = upperBound
                			if destination in stopslist:
                    				return source, destination
                			else:
                    				self.speak('Could you please enter a valid destination stop')
                    				continue
       		else:
            		self.speak('Could you please enter a valid boarding point')
           		continue
	stops = {'vizag','sec','hyd','abc'}
	source, destination = enter_source_destination(stops)
	self.speak('The sourceing point is '+ source+ 'and the destination is '+ destination)
	
	def stop(self):
		pass
	
def create_skill():
	return checkingSkill()
