money = input("How much money to you have right now? ")
ps4 = 21000
afford = money/ps4
print "The value of PlayStation 4 today is", ps4
print "You can afford", afford, "PlayStation 4 as of now."
print "You still need", ps4 - abs(money - (afford * ps4)), "in order to buy another PlayStation 4."
