#!/usr/bin/python

# This script simply generates a table of the voltage to expect
# if I combine my photoresistors with some of my resitors from stock..

# As there is no strong sunlight at the moment here, I will have to
# postpone the real life testing..

voltage=5.

resistor=[59,180,220,453,750,1000,10000,20000]
measurement=[2000000, 1000000, 600000, 200000, 100000, 80000, 40000, 20000, 10000, 8000, 6000, 4000, 2000, 1000, 800, 600, 400, 200, 100, 80, 60, 40, 20, 8, 2]

def measure(r,p):
    return round(voltage/(r+p)*r,4)

print ""
print "Table of expected voltage for a given resistor and light exposure"
print "-----------------------------------------------------------------"
print ""
print "Setup:"
print " -----[R]---+--(~)---- 5V"
print " |          |"
print " = 0V      {?}"
print "            |"
print "            = 0V"
print ""

s="~ \\ R\t"
for r in resistor:
    s+=str(r)+"\t"
print s

for m in measurement:
    s=str(m) + "\t"
    for r in resistor:
        s+=str(measure(m,r)) + "\t"
    print s



 
