names = list()
while True:
    name = raw_input("Skriv ett namn: ")
    if name == 'END':
        break
    names.append(name)
    
names.sort()
for name in names :
    print name