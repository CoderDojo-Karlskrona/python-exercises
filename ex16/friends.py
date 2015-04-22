from friendclass import *

friends = list()

while True:
    name = raw_input("Namn: ")
    if name == 'END':
        break
    number = raw_input("Tfn: ")
    if number == 'END':
        break
     
    friends.append(Friend(name, number))
    
print "----------------"
    
for friend in friends:
    print friend.toString()