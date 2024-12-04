#!/bin/python

import sys
import re

def checkStarOne(l):
  muls = re.findall("(mul\\((\\d{1,3}),(\\d{1,3})\\))",l)
  # print(muls)
  sum = 0
  for mul in muls:
    sum += int(mul[1])*int(mul[2])
  return sum

def checkStarTwo(l, do):
  muls = re.findall("((mul\\((\\d{1,3}),(\\d{1,3})\\))|(do\\(\\))|(don't\\(\\)))",l)
  print(muls)
  sum = 0
  # do = True
  for mul in muls:
    print(mul)
    if mul[4] != '':
      do = True
    elif mul[5] != '':
      do = False
    elif do:
      sum += int(mul[2])*int(mul[3])
      print("%d * %d" % (int(mul[2]),int(mul[3])))
  return (sum, do)


with open(sys.argv[1], 'r') as file:
  totalSum = 0
  for l in file:
    s =  checkStarOne(l)
    print("Sum: %d" % s)
    totalSum += s
  print("Total %d" % totalSum)

with open(sys.argv[1], 'r') as file:
  totalSum = 0
  do = True
  for l in file:
    (s, do) =  checkStarTwo(l, do)
    print("Sum: %d" % s)
    totalSum += s
  print("Total %d" % totalSum)

