import random

s="abcdABCD1234!@#$"
passlen=8
p="".join(random.sample(s,passlen))
print p
