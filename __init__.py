from adapt.intent import IntentBuilder
from mycroft import intent_handler

class PotatoSkill(MycroftSkill):
	
	 @intent_handler(IntentBuilder().require(PythonPerson).require(WhereFrom))
    def handle_from(self, message):
        # PythonPerson can be any of the Monty Python members
        python = message.data.get('PythonPerson')
        self.speak('He is from {}'.format(from_dict[python]))
        self.set_context('PythonPerson', python)
        self.set_context('Location', from_dict[python])
	
	
def create_skill():
    return PotatoSkill()
