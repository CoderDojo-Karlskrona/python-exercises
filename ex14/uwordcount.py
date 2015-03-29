fh = open("../data/words.txt")
uwords = dict()
for line in fh:
    for word in line.split():
        uwords[word] = uwords.get(word, 0) + 1

mostCommonWord = ""
mostCommonWordCount = 0
for word in uwords:
    if uwords.get(word) > mostCommonWordCount:
        mostCommonWord = word
        mostCommonWordCount = uwords.get(word)

print "Unika ord: " + str(len(uwords))
print "Vanligaste ordet: " + mostCommonWord
