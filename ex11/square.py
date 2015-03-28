def square(height, length):
    return height * length

try:
    length = float(raw_input("Length: "))
    height = float(raw_input("Height: "))
    print "Area : " + str(square(height, length))
except:
    print "Not a correct number"
