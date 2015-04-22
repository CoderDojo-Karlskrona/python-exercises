from friendclass import *

def readFriends(fname, friendList):
    fh = open(fname)
    for line in fh:
        splitted = line.split()
        friendList.append(Friend(splitted[0], splitted[1]))
    fh.close()

def writeFriends(fname, friendList):
    fh = open(fname, 'w')
    for friend in friends:
        fh.write(friend.toString())
        fh.write('\n')
    fh.close()

def printList(friends):
    print "-------FRIENDS---------"
    for friend in friends:
        print friend.toString()    
    print "-----------------------"

# read all friends from file
fileName = "friends.txt"
friends = list()
readFriends(fileName, friends)
printList(friends)

# get input from user
while True:
    name = raw_input("Namn: ")
    if name == 'END':
        break
    number = raw_input("Tfn: ")
    if number == 'END':
        break
     
    friends.append(Friend(name, number))
    
# print friends and store them
printList(friends)
writeFriends(fileName, friends)