# (C) copyright 2018 Martin Lurie   Sample code, not supported

# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6598339/
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
maxrows=10000000
# create a reference number for the curve
maxrows=maxrows+10000000
for numrows in range (10000000, maxrows):
  print (numrows+1, end='|')
  L=abs(random.gauss(.7,.3 ))
  x0=random.gauss(0,1 )
  #xlist=[]
  dt=0
  #ylist=[]
  k=random.gauss(1,.5 )
  x=-6
  label=0  # 0 norm
  fast=0
  while ( x < 6 ):
    y=L/(1+math.exp(-k*(x-x0)))
#    ylist.append(y)
#    xlist.append(dt)
    dt=dt+1
    print (y, end='|')
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
#  print ("")
#  print (xlist)
#  print(ylist)
  
# importing the required module 
# python gencurves.py | gzip > clotcuves.gz
# !hadoop fs -mkdir s3a://cdp-sandbox-default-se/datalake/marty
# !hadoop fs -mkdir s3a://cdp-sandbox-default-se/datalake/marty/clotcuves

# !hadoop fs -put clotcurves.gz  s3a://cdp-sandbox-default-se/datalake/marty/clotcuves

# !hadoop fs -ls s3a://cdp-sandbox-default-se/datalake/marty/clotcuves
