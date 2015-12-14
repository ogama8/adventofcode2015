import hashlib

secret = "iwrupvqb"

number = 0
while hashlib.md5(secret + str(number)).hexdigest()[:5] != "00000":
   number += 1

print number
