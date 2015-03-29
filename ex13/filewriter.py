sentences = list()

while True:
    txt = raw_input("Skriv en mening: ")
    if txt == 'END':
        break
     
    sentences.append(txt)
    
outFile = open('mywords.out', 'w')
for sentence in sentences:
    outFile.write(sentence)
    outFile.write('\n')
outFile.close()

# empty line
print ""

fh = open("mywords.out")
for line in fh:
    print line.rstrip().upper()
