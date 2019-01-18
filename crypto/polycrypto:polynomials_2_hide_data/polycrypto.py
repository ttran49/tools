#! /usr/bin/python

#https://en.wikipedia.org/wiki/Finite_field_arithmetic#Effective_polynomial_representation

# IF there is a +1 at the end, replace that with a 0 at the right
# the number 1 here mean just x^1 aka x
position=[206,205,202,201,198,197,195,194,190,189,184,182,181,178,177,176,174,173,172,171,169,168,166,165,164,157,156,150,149,147,146,142,141,140,139,136,134,133,131,130,129,126,125,123,122,121,120,118,117,115,114,112,109,108,104,102,101,96,94,93,91,90,86,85,84,81,80,78,76,75,74,73,72,69,68,66,62,61,60,57,53,52,49,48,46,44,43,42,41,40,38,37,35,33,32,29,28,21,20,14,13,11,10,6,5,4,3,2,0]

highest = max(position)

pad = 8 - (highest % 8) #pad to a full 8bits 
leng= highest + pad
binary=""

for i in range(0,leng):
	if i in position:
		binary+="1"
	else:
		binary+="0"

binary = binary[::-1]

#print binary
print hex(int(binary,2))[2:-1].decode('hex')