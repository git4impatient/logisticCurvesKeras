#!/usr/bin/bash
# (C) copyright 2018 Martin Lurie   Sample code, not supported
#
#
#export NUMROWS=10000000
#./gendata.py 1000000 > mydata.txt
#ls -l

!hadoop fs -rm -r  s3a://cdp-sandbox-default-se/datalake/marty
!hadoop fs -mkdir   s3a://cdp-sandbox-default-se/datalake/marty
!hadoop fs -mkdir s3a://cdp-sandbox-default-se/datalake/marty/clotcuves
!python 200gencurves.py | gzip >clotcurves.gz 
#hadoop fs -put - s3a://cdp-sandbox-default-se/datalake/marty/clotcuves/clotcuves.gz

!hadoop fs -put clotcurves.gz  s3a://cdp-sandbox-default-se/datalake/marty/clotcuves

!hadoop fs -ls s3a://cdp-sandbox-default-se/datalake/marty/clotcuves


