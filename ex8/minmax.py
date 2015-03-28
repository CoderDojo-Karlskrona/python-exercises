values = list()
while True:
    txt = raw_input("Skriv ett heltal: ")
    if txt == 'END':
        break
     
    values.append(int(txt))

# Solution 1 - Use min/max functions the list
print "Min=" + str(min(values))
print "Max=" + str(max(values))


# Solution 2 - Sort the list and get the first/last item in the list
values.sort()
print "Min=" + str(values[0])
print "Max=" + str(values[len(values) - 1])

# Solution 3 - Loop the list and find the min/max values
minVal = None
maxVal = None
for value in values:
    if value > maxVal or maxVal == None:
        maxVal = value
    if value < minVal or minVal == None:
        minVal = value

print "Min=" + str(minVal)
print "Max=" + str(maxVal)
