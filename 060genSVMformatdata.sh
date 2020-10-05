#!/usr/bin/bash
# (C) copyright 2018 Martin Lurie   Sample code, not supported
#
#
#export NUMROWS=10000000
#./gendata.py 1000000 > mydata.txt
#ls -l

!hadoop fs -rm -r  s3a://cdp-sandbox-default-se/datalake/marty/clotcurvesSVM
#!hadoop fs -mkdir   s3a://cdp-sandbox-default-se/datalake/marty/clotcurves
!hadoop fs -mkdir s3a://cdp-sandbox-default-se/datalake/marty/clotcurvesSVM
#!python 200gencurves.py | gzip >clotcurves.gz 
#hadoop fs -put - s3a://cdp-sandbox-default-se/datalake/marty/clotcuves/clotcuves.gz
# no local store go direct to S3

# svm format can't read a gz file !python 210gencurvesSVM.py | gzip | hadoop fs -put -   s3a://cdp-sandbox-default-se/datalake/marty/clotcurvesSVM/clotcurvesSVM.gz

!python 210gencurvesSVM.py | hadoop fs -put -   s3a://cdp-sandbox-default-se/datalake/marty/clotcurvesSVM/clotcurvesSVM

#!hadoop fs -put clotcurves.gz  s3a://cdp-sandbox-default-se/datalake/marty/clotcurves

!hadoop fs -ls s3a://cdp-sandbox-default-se/datalake/marty/clotcurvesSVM


