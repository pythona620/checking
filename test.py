from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler, intent_file_handler
stops = ['vizag', 'hyderabad', 'vijayawada']
class ticket(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    
    @intent_handler(IntentBuilder("travel").require("travel").build())
    
    def handle_travel_intent(self, source,destination):
        
#     def getstop(self,source,destination):
        source = []
	    destination = []
	    while true:
            source = (source.data.get('source')
	  	    if source in stops:
	  		    while True:
                    destination = (source.data.get('destination')               
                # destination = input('Enter your destination: ')
                    if destination in stops:
                        return source, destination
                    else:
                        self.speak_dialog('vaild.destination')
                        continue
            else:
                self.speak_dialog('vaild.boarding')
                continue
     def stop(self):
             source,destination = getstops(stops)
             self.speak("your friend is going " + source  + " " + "to" + " "+  destination ) 
                                   
        pass

def create_skill():
    return ticket()
