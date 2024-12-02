#!/bin/python

import sys

left = []
right = []

with open(sys.argv[1], 'r') as file:
  for l in file:
    nums = l.split()
    left.append(int(nums[0]))
    right.append(int(nums[1]))
    print("L %s  %d %s" % (l, int(nums[0]), int(nums[1])))

leftS = left.copy()
rightS = right.copy()

leftS.sort()
rightS.sort()

print(left)
print(right)

diff = []

sum = 0;

for i in range(len(left)):
  print(abs(leftS[i]-rightS[i]))
  sum += abs(leftS[i]-rightS[i])

print("Sum = ", sum)

mulSum = 0

for i in range(len(left)):
  temp = left[i]*right.count(left[i])
  print("%d * %d = %d" %(left[i],right.count(left[i]),temp))
  mulSum += temp

print("Multiplied sum = ", mulSum)


