#! /usr/bin/python
import gmpy2

'''
    e: 3
    c:219878849218803628752496734037301843801487889344508611639028
    n:245841236512478852752909734912575581815967630033049838269083 

Obviously, e is the public key index, c is the ciphertext, and n is the large number.

First of all, I tried to use the lowe method to use the 3 cipher text, if not, add n and then open the square. 
But tried and added a lot of n did not open into an integer.

Also see that the value of n is not large, you should be able to find two prime factors p and q of n. 
Using the factorization database http://factordb.com, it was found that n can be decomposed into two prime numbers. 
After knowing the two prime numbers, we can quickly get the private key through the public key e. 
'''

#provided in ctf 
e=gmpy2.mpz(65537)
c=gmpy2.mpz(684151956678815994103733261966890872908254340972007896833477109225858676207046453897176861126186570268646592844185948487733725335274498844684380516667587)
n=gmpy2.mpz(14783703403657671882600600446061886156235531325852194800287001788765221084107631153330658325830443132164971084137462046607458019775851952933254941568056899)

# p and q obtained by factorization from n
# http://factordb.com 
p=gmpy2.mpz(121588253559534573498320028934517990374721243335397811413129137253981502291629)
q=gmpy2.mpz(121588253559534573498320028934517990374721243335397811413129137253981502291631)

#calculate (p-1)*(q-1) to get phi
phi=gmpy2.mul(p-1,q-1)

#calculate e for phi
d=gmpy2.invert(e,phi)

#c is the d-th power mod n
m=int(gmpy2.powmod(c,d,n))

print hex(m)[2:-1].decode('hex')
