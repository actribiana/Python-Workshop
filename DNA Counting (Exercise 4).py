count = 0
dna = open("dna.txt").read()
for line in open("dna.txt").read():
    lencount = len('dna')
    ccount = dna.count("C")
    gcount = dna.count("G")
    ccp = (ccount / lencount) * 100
    gcp = (gcount / lencount) * 100
    tcp = ccp + gcp
print "This DNA has", ccount, "percent of C DNA."
print "This DNA has", gcount, "percent of G DNA."
print "This DNA has", tcp, "percent of C + G DNAs."
    
    
