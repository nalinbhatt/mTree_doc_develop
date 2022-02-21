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
class InstitutionClass(Institution):
    def __init__(self):
        pass

    @directive_decorator("institution_message")
    def institution_message(self, message:Message):
        
        message_payload = message.get_payload() #accesses the message payload 
        message_sender_address = message.get_sender() #access the sender agent's address
        
        #You can find more on logging in the <logs> section in References 
        self.log_message(f"message_payload = {message_payload}\n") 
        self.log_message(f"message_sender_address = {message_sender_address}\n")

        #
        self.reminder_message()

        
    




     

    
        