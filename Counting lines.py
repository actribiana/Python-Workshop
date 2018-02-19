count = 0
for line in open("random.txt").read():
    count = count + 1
print "The file contains", count, "lines."
