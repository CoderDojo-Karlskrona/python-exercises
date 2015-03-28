score = float(raw_input("Score: "))
if score > 100 or score < 0:
    print "Score out of range"
elif score >= 90:
    print "A"
elif score >= 80:
    print "B"
elif score >= 70:
    print "C"
elif score >= 60:
    print "D"
else:
    print "F"