#!/usr/bin/bash
# (C) copyright 2018 Martin Lurie   Sample code, not supported
#
#
#export NUMROWS=10000000
#./gendata.py 1000000 > mydata.txt
#ls -l

!hadoop fs -rm -r  s3a://cdp-sandbox-default-se/datalake/marty/clotcurves
#!hadoop fs -mkdir   s3a://cdp-sandbox-default-se/datalake/marty/clotcurves
!hadoop fs -mkdir s3a://cdp-sandbox-default-se/datalake/marty/clotcurves
#!python 200gencurves.py | gzip >clotcurves.gz 
#hadoop fs -put - s3a://cdp-sandbox-default-se/datalake/marty/clotcuves/clotcuves.gz
# no local store go direct to S3

!python 200gencurves.py | gzip | hadoop fs -put -   s3a://cdp-sandbox-default-se/datalake/marty/clotcurves/clotcurves.gz

#!hadoop fs -put clotcurves.gz  s3a://cdp-sandbox-default-se/datalake/marty/clotcurves

!hadoop fs -ls s3a://cdp-sandbox-default-se/datalake/marty/clotcurves


