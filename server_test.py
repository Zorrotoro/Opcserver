
import random
from time import sleep


import opcua
#Import OPCUA 



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

workpieceID=param.add_variable(addspace,"Workpiece ID","nil")
#Adding a variable (workpieceID) to the parameter (param), by assigning False as the initial value.

temperature.set_writable()
#Setting the temperature variable to be writable (can be updated).

Coolant.set_writable()
#Setting the Coolant variable to be writable (can be updated).

workpieceID.set_writable()
#Setting the workpieceID variable to be writable (can be updated).

flag_var=False


@opcua.uamethod
def start_a_machining_operation(parent,flag):
    
    global flag_var
    flag_var=flag

    global workpieceID

    workpieceID.set_value("Operation_lathe"+str(random.randint(0,100))) #Assigning a workpiece ID to the workpieceID variable

    Remaining_time=random.randint(10,16)
    #Set a random fix value to the program remaining run time which in real world is a variable
    print("ready")

    return Remaining_time #Returning remaining time


@opcua.uamethod
def coolant_status_on(parent):
    
    Coolant.set_value(True)

    #Turning On Coolant
    return 0


@opcua.uamethod
def coolant_status_off(parent):
    
    Coolant.set_value(False)
    #Turning Off Coolant
    return 0


opc_object.add_method(1,"Lathe Operation A", start_a_machining_operation)
opc_object.add_method(1,"Coolant Management", coolant_status_on )
opc_object.add_method(1,"Coolant Management", coolant_status_off )
#Adding OPC Method to the Python OPC Objects



myserver.start()
#Starting the server
while True:

    
    if flag_var: #Temperature of tool during operation
        temperature_Var=round(random.uniform(60,100),1)
        #Generating a random value from 60.0 to 100.0 to simulate the machinging temperature going up

    else: #Temperature of tool during operation
        temperature_Var=round(random.uniform(20,30),1)
         #Generating a random value from 20.0 to 30.0 to simulate the temperature at the standby mode

    temperature.set_value((str(temperature_Var)))
    #Setting the random generated value to the temperature variable in opc ua server


    sleep(1)
