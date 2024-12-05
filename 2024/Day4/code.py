#!/bin/python

import sys
import re

class NullLetter:
  def __init__(self):
    self.letter = '*'

class Letter:
  def __init__(self, letter):
    self._letter = letter
    self.links = [NullLetter(),NullLetter(),NullLetter(),NullLetter(),NullLetter(),NullLetter(),NullLetter(),NullLetter()]
  
  def __repr__(self):
    return self._letter

  def __str__(self):
    return "%s %s\n %s \n%s %s" %(self.links[4].letter,self.links[5].letter,self._letter, self.links[6].letter,self.links[7].letter)
    # return "Letter %s {left: %s, up: %s, right: %s, down: %s}" %(self._letter, self.links[0].letter,self.links[1].letter,self.links[2].letter,self.links[3].letter)
  
  def FindInLinks(self, letter):
    ret = []
    for l in self.links:
      if l.letter == letter:
        ret.append(l)
    return ret

  def FindWordInLinks(self, word):
    t = 0
    for l in range(8):
      local = self
      f = True
      for let in word:
        if local.links[l].letter == let:
          local = local.links[l]
        else:
          f = False
          break
      if f:
        t += 1
    return t

  @property
  def letter(self):
    return self._letter[0]

  @property
  def left(self):
    return self.links[0]
  
  @left.setter
  def left(self, value):
      self.links[0] = value
  
  @property
  def right(self):
    return self.links[2]
  
  @right.setter
  def right(self, value):
      self.links[2] = value
  
  @property
  def up(self):
    return self.links[1]
  
  @up.setter
  def up(self, value):
      self.links[1] = value

  @property
  def down(self):
    return self.links[3]
  
  @down.setter
  def down(self, value):
      self.links[3] = value

  @property
  def d1(self):
    return self.links[4]
  
  @d1.setter
  def d1(self, value):
      self.links[4] = value
  
  @property
  def d2(self):
    return self.links[5]
  
  @d2.setter
  def d2(self, value):
      self.links[5] = value
  
  @property
  def d3(self):
    return self.links[6]
  
  @d3.setter
  def d3(self, value):
      self.links[6] = value

  @property
  def d4(self):
    return self.links[7]
  
  @d4.setter
  def d4(self, value):
      self.links[7] = value

exes = []

def checkStarOne(g,x):
  h = len(g)
  w = len(g[0])

  t = 0

  for i in range(h):
    print(len(g[i]))
    for j in range(w):
      print(j)
      if i != 0:
        g[i][j].up = g[i-1][j]
      if j != 0:
        g[i][j].left = g[i][j-1]
      if j != w-1:
        g[i][j].right = g[i][j+1]
      if i != h-1:
        g[i][j].down = g[i+1][j]

      if i != 0 and j != 0:
        g[i][j].d1 = g[i-1][j-1]
      if i != 0 and j != w-1:
        g[i][j].d2 = g[i-1][j+1]
      if i != h-1 and j != 0:
        g[i][j].d3 = g[i+1][j-1]
      if i != h-1 and j != w-1:
        # print(i,j,h,w)
        # print(g[i+1])
        g[i][j].d4 = g[i+1][j+1]
      print(g[i][j])

  print("Printing x's")
  # for xx in x:
  #   ms = xx.FindInLinks('M')
  #   found = False
  #   print(xx)
  #   for m in ms:
  #     aas = m.FindInLinks('A')
  #     print(aas)
  #     for a in aas:
  #       ss = a.FindInLinks('S')
  #       print("S: ", ss)
  #       print("S: ", a)
  #       # t += len(ss)
  #       found = True
  #   if found:
  #     t += 1

  for xx in x:
    tt = xx.FindWordInLinks('MAS')
    print(tt)
    t += tt

  t = 0
  
  for a in ayes:
    # if 
    # tt = a.FindWordInLinks('MAS')
    # print(a)
    # print()
    # print(a.d1.letter, a.d4.letter)
    # print(a.d2.letter, a.d3.letter)
    # print()
    # print()
    if (a.d1.letter == 'M' and a.d4.letter == 'S') or (a.d1.letter == 'S' and a.d4.letter == 'M'):
      print("Pass first")
      if (a.d2.letter == 'M' and a.d3.letter == 'S') or (a.d2.letter == 'S' and a.d3.letter == 'M'):
        print("Found: ", a)
        t += 1


    # t += tt


    # print(x[l])
    # if x[l].right.letter == 'M' and x[l].right.right.letter == 'A' and x[l].right.right.right.letter == 'S':
    #   print(x[l])
    #   t += 1
    # if x[l].left.letter == 'M' and x[l].left.left.letter == 'A' and x[l].left.left.left.letter == 'S':
    #   print(x[l])
    #   t += 1
    # if x[l].up.letter == 'M' and x[l].up.up.letter == 'A' and x[l].up.up.up.letter == 'S':
    #   print(x[l])
    #   t += 1
    # if x[l].down.letter == 'M' and x[l].down.down.letter == 'A' and x[l].down.down.down.letter == 'S':
    #   print(x[l])
    #   t += 1

  return t

grid = []

ayes = []

with open(sys.argv[1], 'r') as file:
  totalSum = 0
  for l in file:
    gridLine = []
    for c in l:
      print("Char %s" % c)
      if c in "XMAS.":
        gridLine.append(Letter(c))
      if c == 'X':
        exes.append(gridLine[-1])
      if c == 'A':
        ayes.append(gridLine[-1])
    grid.append(gridLine)
  print("Grid:\n",grid)
  print("X's\n", exes)

  t = checkStarOne(grid,exes)

  print(t)

