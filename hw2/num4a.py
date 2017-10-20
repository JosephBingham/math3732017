import math

#degree 3, found by using rrech of varible matrix
f = lambda x: 3*x*math.e**x - math.e**(2*x)
df = lambda x: 3*math.e**x + 3*x*math.e**x - 2*math.e**(2*x)
cooef = [1.440418999990135, -7.624829999971098, 11.694199999971794 ,-4.743999999990829]
ansd3 =0
for c in xrange(len(cooef)):
	ansd3 += (1.03)**c * cooef[c]
print "degree 3: ", ansd3
print f(1.03)
print "error : ", ansd3 - f(1.03)

#degree 5, found by using rrech of varible matrix
cooef =[-1.274338856423367, 2.472088954744194, -1.8224693372779122, 2.3672481600678665, 0.4863798451622997, -0.49036107594861567]
ansd5 = 0
for c in xrange(len(cooef)):
	ansd5 += (1.03)**c * cooef[c]
print "degree 3: ", ansd5
print f(1.03)
print "error : ", ansd5 - f(1.03)


