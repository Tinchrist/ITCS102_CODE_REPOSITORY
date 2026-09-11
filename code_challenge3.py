
#DISPLAY
print("______________________________________________________________________________________________")

SenderName = input('Enter the name of the sender --> ')

print("______________________________________________________________________________________________")

Itemtype = input('What is the type of item did you purchase ? --> ')

print("______________________________________________________________________________________________")

is_Fragile = bool(input('Is the item fragile? (yes or no) --> ') == 'yes')

print("______________________________________________________________________________________________")

Weight = float(input('How heavy is the item in kg? --> '))

print("______________________________________________________________________________________________")

Distance = float(input('How far is the item from the designated destination in km? --> '))

print("______________________________________________________________________________________________")

is_Express = bool(input('Does it need to be shipped immediately? (yes or no) --> ') == 'yes')

print("______________________________________________________________________________________________")

is_International = bool(input('Does this item come from overseas? (yes or no) --> ') == 'yes')

print("______________________________________________________________________________________________")



#COMPUTATION
base_cost = (Weight * 2.5) + (Distance * 0.15)

if Distance <= 100 and Weight <= 2 and not is_Express and not is_International:
    Total = 0

elif is_International and is_Express:
    Total = (base_cost * 1.4) + 50

elif Weight > 20 and is_International or is_Express:
    Total = (base_cost * 1.2) + 25

elif Distance > 1000 or Weight > 30:
    Total = base_cost + 30

else:
    Total = base_cost

Shipping_Fee = Total - base_cost



#RESULTS
print('``````````````````````````````````````````````````````````````````````````````````````````````')
print("~DELIVERY INFO~")
print('Sender:', SenderName)
print('Purchase:', Itemtype)
print('Fragile:', is_Fragile)
print('Weight:', Weight, 'kilograms')
print('Distance:', Distance, 'kilometers')
print('Express:', is_Express)
print('International:', is_International)
print('Base Cost: ₱', base_cost)
print('Shipping Fee: ₱', Shipping_Fee)
print('Total: ₱', Total)
print('``````````````````````````````````````````````````````````````````````````````````````````````')

