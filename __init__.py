from mycroft.skills.context import adds_context, removes_context
from mycroft import MycroftSkill

class TomatoSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('PythonPerson').require('Length'))
    def handle_length(self, message):
        python = message.data.get('PythonPerson')
        self.speak('{} is {} cm tall'.format(python, length_dict[python]))

    @intent_handler(IntentBuilder().require('PythonPerson').require('WhereFrom'))
    def handle_from(self, message):
        python = message.data.get('PythonPerson')
        self.speak('{} is from {}'.format(python, from_dict[python]))
   
    def stop(self):
		    pass

def create_skill():
	return TomatoSkill()
   
