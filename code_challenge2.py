money = 4488

print("money to spend", money)

Tsand = (money//1000)
money = (money - Tsand*1000)
Fhundreds = (money//500)
money = (money - Fhundreds*500)
Thundreds = (money//200)
money = (money - Thundreds*200)
ohundreds = (money//100)
money = (money - ohundreds*100)
Fifty = (money//50)
money = (money - Fifty*50)
Twenty = (money//20)
money = (money - Twenty*20)
Ten = (money//10)
money = (money - Ten*10)
Five = (money//5)
money = (money - Five*5)
One = (money//1)
money = (money - One*1)

print("you hold a thousand bills worth",Tsand,"each")
print("you hold a fivehundreads bills worth",Fhundreds,"each")
print("you hold a twohundreds bills worth",Thundreds,"each")
print("you hold a onehundreds bills worth",ohundreds,"each")
print("you hold a fifty bills worth",Fifty,"each")
print("you hold a twenty bills worth",Twenty,"each")
print("you hold a ten bills worth",Ten,"each")
print("you hold a five bills worth",Five,"each")
print("you hold a one bills worth",One,"each")
















