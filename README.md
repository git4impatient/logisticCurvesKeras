# logisticCurvesKeras
(C) Copyright 2020 Martin Lurie
Steps:
- If using TF and Keras run the setup script 040setup which does a pip3 install (without root :-) 
- Open a session and run the 100curveGraph.py - run multiple times to see the different curve shapes
- Update file location in 050gendata and run it - it calls 200gencurves
- SparkML works eaisly with SVM format data, generated with 060genSVMformatdata.sh
- Create table with Impala using 500cols.ddl
- Keras analsys with 300clotKeras
- SparkML - 6+million rows with 350pysparkml.classifier.py
