from enum import Flag
import random
from time import sleep


import opcua
#Import OPCUA 

from opcua import uamethod

myserver = opcua.Server()
#Creating server instance

url="localhost"
endpoint = "opc.tcp://"+url+":5002"  
myserver.set_endpoint(endpoint)
#Establishing Server endpoint

name="OPC_lathe"
addspace= myserver.register_namespace(name)
#Registering a namespace for the server

opc_object = myserver.get_objects_node()
#Creating a OPC object

param=opc_object.add_object(addspace,"parameter")
#Adding a parameter (param) to the object.

temperature=param.add_variable(addspace,"Temperature","0 c")
#Adding a variable (temperature) to the parameter (param), by assigning 0 as the initial value.

Coolant=param.add_variable(addspace,"Coolant",False)
#Adding a variable (Coolant) to the parameter (param), by assigning False as the initial value.

temperature.set_writable()
#Setting the temperature variable to be writable (can be updated).

Coolant.set_writable()
#Setting the Coolant variable to be writable (can be updated).

flag_var=False

#Method to initiate Lathe Operation
@uamethod
def initiateOperation(parent,flag):
    
    global flag_var
    flag_var=flag
    return 0


opc_object.add_method(1,"Lathe Operation A", initiateOperation )
#Adding OPC Method to the Python OPC Objects



myserver.start()
#Starting the server
while True:

    if flag_var: #Temperature of tool during operation
        temperature_Var=round(random.uniform(60,70),1)
        #Generating random value from 50.0 to 60.0

    else: #Temperature of tool during operation
        temperature_Var=round(random.uniform(50,60),1)
        #Generating random value from 50.0 to 60.0

    temperature.set_value((str(temperature_Var)+(" c")))
    #Setting the random generated value to the temperature variable in opc ua server


    sleep(1)
