from time import sleep
from opcua import Client
#Import OPCUA client module

#Enter the OPC UA endpoint url

url = "opc.tcp://localhost:5002"
client=Client(url)
#Create client instance

client.connect()
#Connect to the server

Temperature_variable = client.get_node("ns=2;i=2")
#Create Temperature variable using right node ID
print(Temperature_variable.get_value())
#Get the value for the Temperature variable and print


Coolant_variable = client.get_node("ns=2;i=3")
#Create Coolant variable using right node ID
Coolant_variable.set_value(True)
#Set the value for the Coolant variable

print(Coolant_variable.get_value())
#Get the value for the Coolant variable and print


objects_node = client.get_objects_node()
#Get Root Object nodes from OPC Server

method=client.get_node("ns=1;i=2001")
#Create a Method variable using method node ID


flag=True
#Local variable

objects_node.call_method(method,flag)
#Call method from OPC server by passing right Method ID and passing a local variable

sleep(1)

print(Coolant_variable.get_value())
#Get the value for the Coolant variable and print

print(Temperature_variable.get_value())
#Get the value for the Temperature variable and print
