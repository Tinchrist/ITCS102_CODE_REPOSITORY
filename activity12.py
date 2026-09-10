import getpass

username = 'chrizzy'
password = 'stevenuniverse1'

u = input( 'Input Username ----> ')
p = getpass.getpass( 'Input Password ----> ')

if username == u and p == password :
		print("ACCESS GRANTED")
else : 
		print("ACCESS DENIED")