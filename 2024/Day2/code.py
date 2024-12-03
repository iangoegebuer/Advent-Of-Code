#!/bin/python

import sys

safe = 0
safe2 = 0

def checkSafeStarOne(l):
    nums = l.split()
    s = True
    s2 = 0
    f = 0;
    for i in range(len(nums)):
      if i == 0:
        continue
      np = int(nums[i])
      nk = int(nums[i-1])
      fp = np - nk
      if fp == 0:
        s = False
        s2 += 1
        continue
      fp = abs(fp)/fp
      if i == 1:
        f = np - nk
        f = abs(f)/f
      if abs(nk - np) == 0 or abs(nk - np) > 3:
        s = False
        s2 += 1
        continue
      if i > 1 and fp != f:
        s = False
        s2 += 1
        continue
      
    print("L %s %s" % (l[:-1],
          "safe" if s else "unsafe"))

    return s

def checkSafeStarTwo(l):
    numsFull = l.split()
    s = True
    s2 = 0
    f = 0;
    skip = 0
    for j in range(len(numsFull)):
      s = True
      f = 0;
      nums = numsFull.copy()
      nums.pop(j)
#      print(nums)
      s = checkSafeStarOne(" ".join(nums))
      if s:
        print("Safe if skip %s" % (numsFull[j]))
        return True
        break
#    print("L %s %s" % (l[:-1],
#          "safe" if s else "unsafe"))

    return False





with open(sys.argv[1], 'r') as file:
  for l in file:
    s =  checkSafeStarOne(l)

    if s:
      safe += 1
      safe2 += 1
      continue

    s2 = checkSafeStarTwo(l)

    if s2:
      safe2 += 1

print("Star 1: ",safe)
print("Star 2: ", safe2)



