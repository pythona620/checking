Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@pythona620 
pythona620
/
Twonumbersadding
1
01
 Code Issues 0 Pull requests 0 Actions Projects 0 Wiki Security Insights Settings
Twonumbersadding/__init__.py / 
@pythona620 pythona620 Update __init__.py
4a9e6d3 5 hours ago
39 lines (33 sloc)  1.08 KB
  
You're using code navigation to jump to definitions or references.
Learn more or give us feedback
# number adding
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger

__author__ = 'pythona620/prasad'
LOGGER = getLogger(__name__)

class NumberAddingSkill(MycroftSkill):

	first_number = 0  
	second_number = 0
	
	def get_numerical_response(self, dialog):
		while True:
			val = self.get_response(dialog)
			try:
				val = int(val) #check the value int or not
				return val
			except ValueError:
				self.speak_dialog("invalid.input")
			except:
				self.speak_dialog("input.error")

	@intent_handler(IntentBuilder("").require("Adding").optionally("Play").optionally("Suggest"))
	def handle_start_game_intent(self, message):
		self.speak_dialog("start.game")

		# get first_numbe
		first_number = self.get_numerical_response("get.first")
		# get second_number
		second_number = self.get_numerical_response("get.second")
		answer = first_number + second_number
		yip=str(answer)
		self.speak_dialog("add.two.numbers.is",{"answer":yip})
	def stop(self):		
		pass
def create_skill():
	return NumberAddingSkill()
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
