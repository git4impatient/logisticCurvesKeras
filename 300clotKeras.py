# (C) copyright 2020 Martin Lurie
## prediction of the outcome or bleeding risk 
## APTT waveform analysis diagnosis
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6598339/
# use pip3 for keras, tensorflow
# thanks to S.V. for the debugging session
# cast all variables to float - used impala and the ddl file
from __future__ import print_function
!echo $PYTHON_PATH
import os, sys
#import path
from pyspark.sql import *

# create spark sql session
myspark = SparkSession\
    .builder\
    .appName("Waveform analsyis with Keras") \
    .config("spark.executor.instances", 4 ) \
    .config("spark.executor.memory", "7g") \
    .config("spark.executor.cores", 2) \
    .config("spark.yarn.access.hadoopFileSystems","s3a://cdp-sandbox-default-se/datalake/")\
    .getOrCreate()


!klist
foo=myspark.sql("select label from curvestage limit 10")
foo.take(50)


import time
print ( time.time())
print (" timestamp "+ time.strftime("%H:%M:%S"))


!klist

print ( myspark )
# make spark print text instead of octal
myspark.sql("SET spark.sql.parquet.binaryAsString=true")

# read in the data file from HDFS
# can do data cleanup in impala as well as here
#
# 
# iotrawdf = myspark.read.parquet ( "/user/hive/warehouse/iotdata_p")
# if comma delimited then: iotrawdf = myspark.read.csv('iotdata.csv', header='true')
#iotrawdf=myspark.read.option("delimiter", "|").csv("iotdata.csv", header="true") 
# also read from s3 mydf = myspark.read.parquet ( "s3a://impalas3a/sample_07_s3a_parquet")
!hadoop fs -cat s3a://cdp-sandbox-default-se/datalake/marty/clotcuves/clotcurves.gz | gunzip  | head

iotdf=myspark.sql('select * from curvestage')
# print number of rows and type of object
#iotdf.cache()
print ( iotdf.count() )
print  ( iotdf )
iotdf.show(5)
## 
#https://medium.com/datadriveninvestor/building-neural-network-using-keras-for-classification-3a3656c726c1

#   
# use pip3 for Python3
# restart may not be required for python3
#!pip3 install --upgrade --force-reinstall tensorflow
#!pip3 install --upgrade --force-reinstall keras
import tensorflow as tf
import keras as ks
from keras import Sequential 
from keras.layers import Dense, Dropout 

from keras.callbacks import TensorBoard as tb


## This runs in the kubernetes-docker CDSW cluster
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
# need dataframe for keras with only numerics 
kerasinputdf=iotdf
kerasinputdf.cache()
kerasinputdf.show(1)
kerasinputdf.count()
kerasinputpsdf=kerasinputdf.toPandas()

kerasinputpsdf.head()
kerasinputpsdf.count()
kerasinputpsdf.describe(include='all')

# data too big sns.heatmap(kerasinputpsdf.corr(), annot=True)
# 

## traindataset at 80% of sample

# train and test split
trainpdf=kerasinputpsdf.sample(frac=0.8,random_state=200)
testpdf=kerasinputpsdf.drop(trainpdf.index)
trainpdf.head()
testpdf.head()


# creating input features and target variables
X= trainpdf.iloc[:,1:121]
y= trainpdf.iloc[:,122]
X.head()
y.head()
#yr=trainpdf.reshape((-1,1))
X.count()
Xnp=X.to_numpy()
ynp=y.to_numpy().reshape(-1,1)
print (Xnp.shape)
print (ynp.shape)
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder(handle_unknown='ignore', sparse=False) 
enc = enc.fit(ynp) 
yhe = enc.transform(ynp) 
#y_test = enc.transform(y_test)
print (yhe.shape)


classifier = Sequential()
#First Hidden Layer
classifier.add(Dense(120, activation='relu', kernel_initializer='random_normal', input_dim=120))
#Second  Hidden Layer
classifier.add(Dense(120, activation='relu', kernel_initializer='random_normal'))
classifier.add(Dropout(0.1))

#Output Layer
classifier.add(Dense(6, activation='softmax', kernel_initializer='random_normal'))
#Compiling the neural network
classifier.compile(optimizer ='adam',loss='categorical_crossentropy', metrics =['accuracy'])

#tbcallback = tb.callbacks.TensorBoard(log_dir='./Graph', histogram_freq=0, write_graph=True, write_images=True)

#Fitting the data to the training dataset
# epocs - how many times do you grind through the training dataset
# batch size - how many samples to examine before updating
#   the model.  You could use a batch size of 1 
#   as the dataset gets bigger batch of 1 will 
#   impact performance
#classifier.fit(X,y, batch_size=10, epochs=50, verbose=1, callbacks=[tbcallback])
# the small batch size of 10 is hurting performance
# moving to 32
#classifier.fit(X,y, batch_size=32, epochs=10, verbose=1)
# loss is erratic - not just going down
# decrease batch size
print ("Model fit start time  "+ time.strftime("%H:%M:%S"))

classifier.fit(Xnp,yhe, batch_size=32, epochs=16, verbose=1,shuffle=False)
print ("Model fit end time "+ time.strftime("%H:%M:%S"))


eval_model=classifier.evaluate(Xnp, yhe)
eval_model

#!pip3 install sklearn

y_pred=classifier.predict(Xnp)
y_pred =(y_pred>0.55)
# confusion matrix - lots of jokes here
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(yhe.argmax(axis=1), y_pred.argmax(axis=1))
print(cm)

# need test data - have we just memorized the input data?


# creating input features and target variables
X= testpdf.iloc[:,1:121]
y= testpdf.iloc[:,122]
X.head()
y.head()
#yr=trainpdf.reshape((-1,1))
X.count()
Xnp=X.to_numpy()
ynp=y.to_numpy().reshape(-1,1)
print (Xnp.shape)
print (ynp.shape)
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder(handle_unknown='ignore', sparse=False) 
enc = enc.fit(ynp) 
yhe = enc.transform(ynp) 
#y_test = enc.transform(y_test)
print (yhe.shape)

eval_model=classifier.evaluate(Xnp, yhe)
eval_model

########################
# optimize - adding dropout improved result
# optimize - more layers?  more cowbell?



y_pred=classifier.predict(Xnp)
y_pred =(y_pred>0.55)
# confusion matrix 
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(yhe.argmax(axis=1), y_pred.argmax(axis=1))
print(cm)

!rm -rf mymodel
#classifier.save ("mymodel")
print (" timestamp "+ time.strftime("%H:%M:%S"))

