# (C)copyright 2020  Martin Lurie 
#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6598339/
# x0 value of the sigmoid's midpoint,
# L = the curve's maximum value,
# k = the logistic growth rate or steepness of the curve.

# to do
# create normal distrib for x0 and classification early norm late
# create normal distrib for L and classification hi low
# encoding:  early-hi earlylow  normhi normlow latehi latelow

from __future__ import print_function
import math
import random

for numrows in range (0, 1):
  L=abs(random.gauss(.7,.3 ))
  x0=random.gauss(0,1 )
  xlist=[]
  dt=0
  ylist=[]
  k=random.gauss(1,.5 )
  x=-6
  label=0  # 0 norm
  fast=0
  while ( x < 6 ):
    y=L/(1+math.exp(-k*(x-x0)))
    ylist.append(y)
    xlist.append(dt)
    dt=dt+1
    #print (y, end='|')
    x=x+.1
    if ( L < .7 and x0 < -.3 ):
      label=1
    if ( L < .7 and x0 > -.3 and x0 < .3):
      label=2
    if ( L<.7 and x0>.3 ):
      label=3
    if ( L > .7 and x0 < -.3 ):
      label=4
    if ( L > .7 and x0 > -.3 and x0 < .3):
      label=5
    if ( L>.7 and x0>.3 ):
      label=6
  
  print (label)
  #print (xlist)
  #print(ylist)
  
# importing the required module 
import matplotlib.pyplot as plt 


def plotit(numpts):
  # plotting the points 
  plt.plot(xlist, ylist) 

  # naming the x axis 
  plt.xlabel('x - axis') 
  # naming the y axis 
  plt.ylabel('y - axis') 
  plt.ylim(0, 1.5)

  # giving a title to my graph 
  plt.title('Sigmoid Curve') 

  # function to show the plot 
  plt.show() 
plotit(5)
print ("L curve max " +str(L) )
print ("x0 is midpoint " + str(x0))
print ("Label for ML is " + str(label))