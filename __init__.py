from mycroft.skills.context import adds_context, removes_context

    @intent_handler(IntentBuilder().require('PythonPerson').require('Length'))
    def handle_length(self, message):
        python = message.data.get('PythonPerson')
        self.speak('{} is {} cm tall'.format(python, length_dict[python]))

    @intent_handler(IntentBuilder().require('PythonPerson').require('WhereFrom'))
    def handle_from(self, message):
        python = message.data.get('PythonPerson')
        self.speak('{} is from {}'.format(python, from_dict[python]))
   
# def stop(self):
# 		pass

# def create_skill():
# 	return NumberGuessSkill()
   
