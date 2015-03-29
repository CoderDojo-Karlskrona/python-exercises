# solution one, loop for each word
fh = open("words.txt")
wordCount = 0
for line in fh:
    for word in line.split():
        wordCount += 1

print "Words: " + str(wordCount)

# solution two, simply count the length of the split
fh = open("words.txt")
wordCount = 0
for line in fh:
    wordCount += len(line.split())

print "Words: " + str(wordCount)
