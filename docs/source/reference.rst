

=========
Reference
=========


.. role:: python(code)
   :language: python

.. _theory_of_operations:

Theory of Operations
====================


- Contains a description and background of Microeconomic Systems and how mTree allows you to define different actors 
- Goes in depth as to why mTree. 
- Need to define why messages are necessary 

.. _messages: 

messages
========

In the :ref:`Actor<Actors>` system, Actors only have access to their personal states. As a result, 
the only way Actors can change their state is through some constant design or by recieving new 
information from a different Actor. 

.. _start_environment:

start_environment
-----------------

The ``start_environment`` message is the very first message that gets sent to the :ref:`environment` Actor (specified in the :ref:`config` file)
after **mTree** initializes everything. 

.. code-block:: python
    
    #inside simulation_folder/mes/environment_file.py

    @directive_enabled_class  
    class EnvironmentClass(Environment):
        def __init__(self):
            pass

        @directive_decorator("start_environment")  
        def start_environment(self, message:Message):
            pass 

.. tip::

    The ``start_environment`` directive can be viewed as the genisis message which gets the ball 
    rolling for all other subsequent messages. Therefore, it is recommended that the directive is 
    used to initialize the environment state as well as send important state information to other Actors. 

.. warning:: 
    
    All mTree simulation need to have a ``start_environment`` :ref:`directive <directive>` specified in 
    the Environment Actor in order to start their simulation. However, messages sent in the ``start_environment`` 
    directive as well as other directives can be based on your design. 

.. _send_message:

How to send a message
---------------------

In order to send a message, the Actor must first receive a message in a :ref:`directive <directive>` first.
Once in a **directive**, the key elements for a message are -

* **Sending Actor's address**: Usually accessed by :code:`self.myAddress` 
* **Content**: This could be any python data type message (None types also work) that you want the other Actor to recieve. 
* **Receiving Actor's address**: This could be accessed several ways, see code example in :ref:`directive <directive>` or checkout :ref:`address_book`

Here is how you can define and send a message-

.. code-block:: python

    new_message = Message() #creates a message object 
    new_message.set_sender(self.myAddress) #self.myAddress is the agent's personal mTree Actor address
    new_message.set_directive("institution_message") #directives are used by message receiving agents to recieve specific messages
    new_message.set_payload("any_python_data_type_would_do") #you can set the payload to any python data type

    self.send(reciever_address, new_message) # This method is used to finally send your message 

|
| In the example below, we continue the ``start_messsage`` directive method in the Environment and send a message 
| to the Institution.
| 

.. code-block:: python

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
            
            self.send(receiver_address, your_message) # This method is used to finally send your message 
        


.. _directive:

Directives / Receiving Messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Directives** are special class methods defined in Actor classes (contained in .py files inside your **mes** folder). 
They are used to view messages sent to the Actor. 
|
| Actors need to have the following in their classes to recieve a particular message. 
| 

.. code-block:: python 

    @directive_decorator("directive_name")
    def directive_name(self, message: Message):

        message_payload = message.get_payload() #accesses the message payload 
        message_sender_address = message.get_sender() #access the sender agent's address

.. warning::  

    In order to recieve a messsage your directive name and your method name need to be the same, otherwise, 
    mTree throws the following :ref:`error<directive_error>`.

.. note::
    For the following example our Actor is set as the :ref:`Institution` type, however, the message receiving process is applicable
    for any type. 

|
| In this above example, the institution receives a message sent by the Environment in :ref:`send message <send_message>`.
|

.. code-block:: python 

    @directive_enabled_class
    class InstitutionClass(Institution):
        def __init__(self):
            pass

        @directive_decorator("institution_message") 
        def institution_message(self, message:Message):#The method name needs to be the same as the directive name set in quotes above
            
            message_payload = message.get_payload() #accesses the message payload 
            message_sender_address = message.get_sender() #access the sender agent's address
            
            #You can find more on logging in the <logs> section in References 
            self.log_message(f"message_payload = {message_payload}\n"
                            f"message_sender_address = {message_sender_address}\n")

Your :ref:`log<log_message>` file should produce the following output -

.. code-block:: ruby

    1645122024.0900638	message_payload = any_python_data_type_would_do

    1645122024.0937853	message_sender_address = ActorAddr-(T|:43253)


First Message - start
---------------------

Sending a message 
-----------------

Receiving a message 
-------------------

Reminder Messages
-----------------

.. _Actors:

Actor Description
=================

.. _environment:

Environment
-----------

.. _institution:

Institution
-----------

.. _agent:

Agent 
-----

.. _config:

config
======

- Description and general layout

mTree use 
---------
- Description of variables used by mTree 
  
Experiment Specific
-------------------
- variables set in properties that can be accesssed by the environment
  
running multiple
----------------

.. _address_book:

address book 
============

Structure
---------

Methods 
-------

How to Distribute and default access 
------------------------------------

.. _logs:

Logs
====

Logging is a way to output key data from a simulation in order to keep track of what the code is doing at various steps. 
mTree provides 2 types of logging capabilities.

- Desription of the 2 types of logging capability that mTree provides 

.. _log_file:

Log File
--------

.. _log_message:

self.log_message(input)
^^^^^^^^^^^^^^^^^^^^^^^

Example 
^^^^^^^
- Shows what a sample log output looks like 
- What all can the log message log.

Best Practice Suggestion
^^^^^^^^^^^^^^^^^^^^^^^^
- Include entry and exit logs. Log variable when certiain important state changes happen. 

.. _data_log:

Data Log 
--------

.. _log_data:

self.log_data(input)

Example
^^^^^^^
- Shows sample output from the .data file 

Interpret into Jupyter notebook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Simple suggestions on how to log data using dictionaries and little code on how pandas could 
be used to read the dataframe. 


.. _error:

Error Handling
==============

.. _directive_error:

Directive name error
--------------------






