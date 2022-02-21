from mTree.microeconomic_system.environment import Environment
from mTree.microeconomic_system.institution import Institution
from mTree.microeconomic_system.agent import Agent
from mTree.microeconomic_system.directive_decorators import *
from mTree.microeconomic_system.message import Message
import math
import random
import logging
import time
import datetime



@directive_enabled_class  
class EnvironmentClass(Environment):
    def __init__(self):
        pass

    @directive_decorator("start_environment")
    def start_environment(self, message:Message):
        
        your_message = Message() #create a message object 
        your_message.set_sender(self.myAddress) #self.myAddress is the agent's personal mTree Actor address
        your_message.set_directive("institution_message") #directives are used by message receiving agents to recieve specific messages
        your_message.set_payload("any_python_data_type_would_do") #you can set the payload to any python data type
        
        #checkout the <address_book> section in References to find how different Actors access each other's addresses
        receiver_address = self.address_book.select_addresses({"short_name":"institution_file.InstitutionClass 1"}) 
        
        your_message.set_recipients(receiver_address)
        self.send(receiver_address, your_message) # This method is used to finally send your message 
        self.get_agents() #TODO: test these address_book methods 







        
        

        



        